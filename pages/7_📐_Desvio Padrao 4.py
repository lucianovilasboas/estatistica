import streamlit as st
import math

# Configuração da página do aplicativo
st.set_page_config(page_title="Cálculo do Desvio Padrão para Dados Agrupados", page_icon="📀", layout="wide")

# Título do aplicativo
st.markdown("<h1 style='text-align: center;'>📀 Cálculo do Desvio Padrão para Dados Agrupados por Intervalo de Classes</h1>", unsafe_allow_html=True)
st.write("Este aplicativo realiza o cálculo da variância e do desvio padrão para dados agrupados inseridos. Informe também se os dados são de uma amostra ou da população.")
st.write("---")

# Entrada para os limites inferiores, superiores e frequências
dados_input = st.sidebar.text_area("""Insira os dados agrupados (siga o formato sugerido):""", placeholder="""10 -- 20: 5\n20 -- 30: 2\n30 -- 40: 8""")

# Tipo de dado: Amostra ou População
eh_amostra = st.sidebar.checkbox("Os dados correspondem a uma amostra?", value=False)

# Converter os dados de entrada em uma lista de tuplas (ponto médio, frequência)
try:
    dados_agrupados = []
    for linha in dados_input.split('\n'): 
        faixa, frequencia = linha.split(':')
        limite_inferior, limite_superior = map(float, faixa.split('--'))
        frequencia = float(frequencia)
        ponto_medio = (limite_inferior + limite_superior) / 2
        dados_agrupados.append((ponto_medio, frequencia))
except ValueError:
    st.error("Por favor, insira os valores corretamente no formato indicado (ex: 10 -- 20: 5), separados por linhas.")
    st.stop()

# Função para calcular a média
def calcular_media(dados_agrupados):
    soma = sum(valor * frequencia for valor, frequencia in dados_agrupados)
    total_frequencia = sum(frequencia for _, frequencia in dados_agrupados)
    return soma / total_frequencia

# Função para calcular a variância
def calcular_variancia(dados_agrupados, media, eh_amostra):
    total_frequencia = sum(frequencia for _, frequencia in dados_agrupados)
    somatorio = sum(frequencia * (valor - media) ** 2 for valor, frequencia in dados_agrupados)
    if eh_amostra:
        variancia = somatorio / (total_frequencia - 1)
    else:
        variancia = somatorio / total_frequencia
    return variancia, somatorio

# Função para calcular o desvio padrão
def calcular_desvio_padrao(variancia):
    return math.sqrt(variancia)

# Botão para calcular
if st.sidebar.button("Calcular"):
    total_frequencia = sum(frequencia for _, frequencia in dados_agrupados)
    if total_frequencia <= 1 and eh_amostra:
        st.error("Para dados de amostra, o total de frequências deve ser maior que 1.")
    else:
        # Cálculo da média
        media = calcular_media(dados_agrupados)
        # Cálculo da variância
        variancia, somatorio = calcular_variancia(dados_agrupados, media, eh_amostra)
        # Cálculo do desvio padrão
        desvio_padrao = calcular_desvio_padrao(variancia)

        # Exibir os resultados com explicações detalhadas
        st.write("## Cálculo:")
        
        # Fórmula da média e seu cálculo
        st.markdown("### Média")
        st.write("A média para dados agrupados é calculada pela fórmula que considera o ponto medio de cada intervalo:")
        st.latex(r"\bar{X} = \frac{\sum (\bar{x_i} \times f_i)}{\sum f_i}")
        dados_somatorio_str = ' + '.join([f'{valor} \\times {frequencia}' for valor, frequencia in dados_agrupados])
        st.latex(f"\\bar{{X}} = \\frac{{{dados_somatorio_str}}}{{{total_frequencia}}} = {round(media, 2)}")
        
        # Fórmula da variância e seu cálculo
        st.markdown("### Variância")
        st.write("A variância é uma medida de dispersão que indica o quão distribuídos os dados estão em relação à média. Para dados agrupados, usa-se a fórmula:")
        st.latex(r"s^2 = \frac{\sum (\bar{x_i} - \bar{X})^2  \times f_i }{n - 1}" if eh_amostra else r"s^2 = \frac{\sum (\bar{x_i} - \bar{X})^2 \times f_i }{n}")
        dados_variancia_str = ' + '.join([f'({valor} - {round(media, 2)})^2 \\times {frequencia} ' for valor, frequencia in dados_agrupados])
        st.latex(f"\\sum (\\bar{{x_i}} - \\bar{{X}})^2 \\times f_i  = {dados_variancia_str} = {round(somatorio, 3)}")
        st.latex(f"s^2 = \\frac{{{round(somatorio, 3)}}}{{{total_frequencia - 1 if eh_amostra else total_frequencia}}} = {round(variancia, 3)}")
        
        # Fórmula do desvio padrão e seu cálculo
        st.markdown("### Desvio Padrão")
        st.write("O desvio padrão é a raiz quadrada da variância e expressa a dispersão dos dados no mesmo nível das médias:")
        st.latex(r"s = \sqrt{s^2}")
        st.latex(f"s = \\sqrt{{{round(variancia, 3)}}} = {round(desvio_padrao, 3)}")

else:
    st.info("Aguardando o cálculo.")