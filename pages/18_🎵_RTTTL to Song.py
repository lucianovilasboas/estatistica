import streamlit as st
from rtttl import parse_rtttl, play_melody, stop_melody, rtttl_to_arduino, generate_arduino_code, parse_rtttl2

# Configuração inicial da página
st.set_page_config(page_title="Conversor RTTTL para Arduino (C++)", page_icon="🎵", layout="wide")
st.markdown("<h1 style='text-align: center;'>🎵 Conversor RTTTL para Arduino (C++)</h1>", unsafe_allow_html=True)

# Introdução ao RTTTL
st.write("""
O RTTTL (Ring Tone Text Transfer Language) é um formato simples para descrever melodias usadas em toques de celular antigos.
Cada código RTTTL contém:
- O nome da melodia.
- Configurações de duração, oitava e BPM (tempo).
- Sequência de notas, incluindo pausas.

Alguns exemplos de código RTTTL:
```
StarWars:d=4,o=5,b=120:c.6,e.6,g6,a6,b6,a6,g6,e6,c.6
```
---
```
MissionImpossible:d=32,o=5,b=125:d6,d#6,d6,d#6,d6,d#6,d6,d#6,d6,d#6,d6,d#6,d6,d#6,d6,d#6,d6,d#6,d6,d#6,e6,f#6,d#6,8g.6,8g.,8g.,8a#,8c6,8g.,8g.,8f,8f#,8g.,8g.,8a#,8c6,8g.,8g.,8f,8f#,16a#6,16g6,2d6,16a#6,16g6,2c#6,16a#6,16g6,2c6,16a#,8c.6,4p,16a#,16g,2f#6,16a#,16g,2f6,16a#,16g,2e6,16d#6,8d.6       

```
---
         
```        
Blue:d=8,o=5,b=140:a,a#,d,g,a#,c6,f,a,4a#,g,a#,d6,d#6,g,d6,c6,a#,d,g,a#,c6,f,a,4a#,g,a#,d6,d#6,g,d6,c6,a#,d,g,a#,c6,f,a,4a#,g,a#,d6,d#6,g,d6,c6,a#,d,g,a#,a,c,f,2g        
```         
---
```
SuperMarioBros:d=4,o=5,b=100:16e6,16e6,32p,8e6,16c6,8e6,8g6,8p,8g,8p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,16p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16c7,16p,16c7,16c7,p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16d#6,8p,16d6,8p,16c6         
```
---
```
Looney:d=4,o=5,b=140:32p,c6,8f6,8e6,8d6,8c6,a.,8c6,8f6,8e6,8d6,8d#6
```
         



                  
""")
st.write("---")

# Entrada do usuário para o código RTTTL
codigo_rtttl = st.text_area("Insira o código RTTTL:", placeholder="Exemplo: StarWars:d=4,o=5,b=120:c.6,e.6,g6,a6,b6,a6,g6,e6,c.6")


# Exibe o código Arduino assim que o campo é preenchido
if codigo_rtttl:
    codigo_rtttl = codigo_rtttl.strip()
    try:

        name, parsed_notes = parse_rtttl2(codigo_rtttl)
        arduino_code = generate_arduino_code(name, parsed_notes)

        # arduino_code = rtttl_to_arduino(codigo_rtttl)
        st.code(arduino_code, language="c")
    except KeyError as ke:
        st.error(f"Nota inválida encontrada: {ke}. Verifique o formato do RTTTL.")
    except Exception as e:
        st.error(f"Erro ao gerar código Arduino: {e}")

col1, col2 = st.columns(2)

with col1:
    if st.button("Tocar Código RTTTL"):
        if codigo_rtttl:
            try:
                st.write(f"Tocando: {codigo_rtttl}")
                melody = parse_rtttl(codigo_rtttl)
                play_melody(melody)
            except Exception as e:
                st.error(f"Erro ao tocar RTTTL: {e}")
        else:
            st.error("Insira um código RTTTL válido!")

with col2:
    if st.button("Parar Música"):
        stop_melody()
