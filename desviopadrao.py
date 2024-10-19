import streamlit as st
import math


st.set_page_config(layout="wide")


# Título do aplicativo
st.title("Cálculo de Variância e Desvio Padrão")

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
    st.latex(f"\\text{{Média}}: \\bar{{X}} = \\frac{{\\sum X}}{{n}} = \\frac{{{' + '.join(map(str, dados))}}}{{{len(dados)}}} = {round(media,2)}")
    st.latex(f"\\text{{Variância}}: \\sigma^2 = \\frac{{\\sum (X_i - \\bar{{X}})^2}}{{n}}")
    st.latex(f"\\sum (X_i - \\bar{{X}})^2 = {' + '.join([f'({x} - {round(media,2)})^2' for x in dados])} = {round(somatorio,2)}")
    st.latex(f"\\sigma^2 = \\frac{{{somatorio}}}{{{len(dados)}}} = {round(variancia,2)}")
    st.latex(f"\\text{{Desvio Padrão}}: \\sigma = \\sqrt{{\\sigma^2}} = \\sqrt{{{round(variancia,2)}}} = {round(desvio_padrao,2)}")
