import streamlit as st
import math

st.set_page_config(page_title="Cálculo de Variância e Desvio Padrão", page_icon="📐",layout="wide")

# Título do aplicativo
st.markdown("<h1 style='text-align: center;'>📐 Cálculo de Variância e Desvio Padrão</h1>", unsafe_allow_html=True)
st.write("Este aplicativo realiza o cálculo da variância e do desvio padrão de um conjunto de dados inseridos.")

# Entrada para os dados
st.sidebar.write("## Insira os dados separados por vírgulas:")
dados_input = st.sidebar.text_area("Exemplo: 1, 2, 3, 4, 5", value="1, 2, 3, 4, 5")

# Converter os dados de entrada em uma lista de floats
try:
    dados = list(map(float, dados_input.split(',')))
except ValueError:
    st.error("Por favor, insira os valores corretamente separados por vírgulas.")

# Função para calcular a média
def calcular_media(dados):
    soma = sum(dados)
    n = len(dados)
    return soma / n

# Função para calcular a variância
def calcular_variancia(dados):
    n = len(dados)
    media = calcular_media(dados)
    somatorio = sum((x - media) ** 2 for x in dados)
    variancia = somatorio / n
    return variancia, somatorio, media

# Função para calcular o desvio padrão
def calcular_desvio_padrao(variancia):
    return math.sqrt(variancia)

if st.sidebar.button("Calcular"):
    variancia, somatorio, media = calcular_variancia(dados)
    desvio_padrao = calcular_desvio_padrao(variancia)

    # Exibir os resultados
    st.write("## Cálculo:")
    if len(dados) > 4:
        dados_somatorio_str = f"{dados[0]} + ... + {dados[-1]}"
        dados_variancia_str = f"({dados[0]} - {round(media,3)})^2 + ... + ({dados[-1]} - {round(media,3)})^2"
    else:
        dados_somatorio_str = ' + '.join(map(str, dados))
        dados_variancia_str = ' + '.join([f'({x} - {round(media,2)})^2' for x in dados])

    st.latex(f"\\text{{Média}}: \\bar{{X}} = \\frac{{\\sum X}}{{n}} = \\frac{{{dados_somatorio_str}}}{{{len(dados)}}} \\ = {round(media,2)}")
    st.latex(f"\\text{{Variância}}: \\sigma^2 = \\frac{{\\sum (X_i - \\bar{{X}})^2}}{{n}}")
    st.latex(f"\\sum (X_i - \\bar{{X}})^2 = {dados_variancia_str} = {round(somatorio,3)}")
    st.latex(f"\\sigma^2 = \\frac{{{somatorio}}}{{{len(dados)}}} = {round(variancia,3)}")
    st.latex(f"\\text{{Desvio Padrão}}: \\sigma = \\sqrt{{\\sigma^2}} = \\sqrt{{{round(variancia,3)}}} = {round(desvio_padrao,3)}")
else:
    st.info("Aguardando o calculo.")