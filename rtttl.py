import simpleaudio as sa
import numpy as np
import re

# Função para converter notas em frequências
NOTE_FREQUENCIES = {
    "c": 261.63, "c#": 277.18, "d": 293.66, "d#": 311.13, "e": 329.63, 
    "f": 349.23, "f#": 369.99, "g": 392.00, "g#": 415.30, "a": 440.00, 
    "a#": 466.16, "b": 493.88, "p": 0  # p represents a pause
}


def note_to_freq(note, octave):
    if note == "p":
        return 0
    return NOTE_FREQUENCIES[note.lower()] * (2 ** (octave - 4))

def parse_rtttl(rtttl):
    name, settings, melody = rtttl.split(":")
    settings = dict(item.split("=") for item in settings.split(","))
    default_duration = int(settings.get("d", 4))
    default_octave = int(settings.get("o", 5))
    bpm = int(settings.get("b", 63))
    
    beat_duration = 60 / bpm * 4  # Duration of a whole note in seconds
    melody = re.findall(r'(\d*)([a-gp#]+)(\d*)(\.*)', melody, re.IGNORECASE)
    
    parsed_melody = []
    for duration, note, octave, dot in melody:
        duration = int(duration) if duration else default_duration
        octave = int(octave) if octave else default_octave
        duration_factor = 1.5 if dot else 1
        note_duration = beat_duration / duration * duration_factor
        note = note.replace('.', '')  # Remove dots from note names for processing
        freq = note_to_freq(note, octave)
        parsed_melody.append((freq, note_duration))
    return parsed_melody

def generate_tone(freq, duration, sample_rate=44100):
    if freq == 0:  # Pause
        return np.zeros(int(sample_rate * duration))
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    return wave

def play_melody(melody, sample_rate=44100):
    global current_play_obj
    audio = np.concatenate([generate_tone(freq, duration, sample_rate) for freq, duration in melody])
    audio = (audio * 32767).astype(np.int16)  # Convert to 16-bit PCM format
    current_play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    current_play_obj.wait_done()

def stop_melody():
    global current_play_obj
    if current_play_obj:
        current_play_obj.stop()
        current_play_obj = None

current_play_obj = None

def rtttl_to_arduino(rtttl, pin=9):
    parts = rtttl.split(':')
    name = parts[0]
    defaults = parts[1]
    melody = parts[2]

    default_settings = {}
    for setting in defaults.split(','):
        key, value = setting.split('=')
        default_settings[key] = int(value)

    default_duration = default_settings.get('d', 4)
    default_octave = default_settings.get('o', 5)
    bpm = default_settings.get('b', 63)

    NOTES = {
        'c': [16, 33, 65, 131, 262, 523, 1046, 2093],
        'd': [18, 37, 73, 147, 294, 587, 1175, 2349],
        'e': [20, 41, 82, 165, 330, 659, 1319, 2637],
        'f': [21, 43, 87, 175, 349, 698, 1397, 2794],
        'g': [24, 49, 98, 196, 392, 784, 1568, 3136],
        'a': [27, 55, 110, 220, 440, 880, 1760, 3520],
        'b': [30, 62, 123, 246, 494, 988, 1976, 3951],
        'p': [0, 0, 0, 0, 0, 0, 0, 0]  # Pause
    }

    ms_per_beat = 60000 // bpm

    code = f'''
int melody[] = {{
'''
    durations = []

    notes = melody.split(',')
    for note in notes:
        duration = default_duration
        octave = default_octave

        if note[0].isdigit():
            duration = int(note[0])
            note = note[1:]

        note = note.replace('#', '').replace('.', '')  # Remove sharp and dots

        if note[-1].isdigit():
            octave = int(note[-1])
            note = note[:-1]

        frequency = NOTES[note][octave - 1]
        duration_ms = ms_per_beat * (4 / duration)

        code += f"  {frequency},"
        durations.append(duration_ms)

    code = code.strip(',') + '};\n\n'
    code += f'int noteDurations[] = {{{", ".join(map(str, durations))}}};\n\n'
    code += f'''
void setup() {{
  for (int thisNote = 0; thisNote < sizeof(melody)/sizeof(melody[0]); thisNote++) {{
    int noteDuration = noteDurations[thisNote];
    tone({pin}, melody[thisNote], noteDuration);
    delay(noteDuration * 1.30);
    noTone({pin});
  }}
}}

void loop() {{
}}
'''

    return code


def parse_rtttl2(rtttl_string):
    # Divide a string RTTTL em seções: nome, parâmetros padrão e notas
    sections = rtttl_string.split(':')
    if len(sections) != 3:
        raise ValueError("Formato RTTTL inválido.")

    name, defaults, notes = sections

    # Processa os parâmetros padrão
    default_settings = {}
    for item in defaults.split(','):
        key, value = item.split('=')
        default_settings[key] = int(value) if key != 'b' else int(value)

    # Define os valores padrão
    default_duration = default_settings.get('d', 4)  # Duração
    default_octave = default_settings.get('o', 6)    # Oitava
    bpm = default_settings.get('b', 63)             # Batidas por minuto

    # Converte BPM em milissegundos por batida
    ms_per_beat = 60000 / bpm

    # Processa as notas
    note_pattern = re.compile(r'(?:(\d+)?)([a-gpA-GP])(#?)(\d*)')
    parsed_notes = []

    for match in note_pattern.finditer(notes):
        duration, note, sharp, octave = match.groups()
        duration = int(duration) if duration else default_duration
        octave = int(octave) if octave else default_octave

        if note.lower() == 'p':  # Pausa
            frequency = 0
        else:
            note_frequencies = {
                'c': 16.35, 'd': 18.35, 'e': 20.60, 'f': 21.83, 'g': 24.50, 'a': 27.50, 'b': 30.87
            }
            frequency = note_frequencies[note.lower()] * (2 ** (octave - 4))
            if sharp:
                frequency *= 2 ** (1 / 12)  # Ajuste para sustenido

        note_duration = ms_per_beat * (4 / duration)
        parsed_notes.append((int(frequency * 9 ), int(note_duration )))  # Luciano adicionou * 9 para aumentar o volume

    return name, parsed_notes


def generate_arduino_code(name, notes):
    melody_array = ", ".join([str(note[0]) for note in notes])
    duration_array = ", ".join([str(note[1]) for note in notes])

    arduino_code = f"// Melodia: {name}\n"
    arduino_code += "#define TONE_PIN 9\n"
    arduino_code += "int melody[] = { " + melody_array + " };\n"
    arduino_code += "int noteDurations[] = { " + duration_array + " };\n\n"

    arduino_code += "void melodia() {\n"
    arduino_code += "  for (int thisNote = 0; thisNote < sizeof(melody)/sizeof(melody[0]); thisNote++) {\n"
    arduino_code += "    int noteDuration = noteDurations[thisNote];\n"
    arduino_code += "    tone(TONE_PIN, melody[thisNote], noteDuration);\n"
    arduino_code += "    delay(noteDuration);\n"
    arduino_code += "    noTone(TONE_PIN);\n"
    arduino_code += "  }\n"
    arduino_code += "}\n\n"


    arduino_code += "void setup() {\n"
    arduino_code += "  pinMode(TONE_PIN, OUTPUT);\n"
    arduino_code += "}\n\n"

    arduino_code += "void loop() {\n"
    arduino_code += "  melodia();\n"
    arduino_code += "  delay(2000);\n"
    arduino_code += "}\n"
    return arduino_code


# # Exemplo de uso
# rtttl_example = "SuperMario:d=4,o=5,b=100:e2,e2,e2,c2,e2,g2,p,a2"
# name, parsed_notes = parse_rtttl2(rtttl_example)
# arduino_code = generate_arduino_code(name, parsed_notes)

# # Salvar o código em um arquivo
# with open("melody.ino", "w") as file:
#     file.write(arduino_code)

# print("Código Arduino gerado com sucesso!")
