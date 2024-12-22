import streamlit as st
import math
import re

# Configuração da página do aplicativo
st.set_page_config(page_title="Cálculo do Desvio Padrão para Dados Agrupados", page_icon="📀", layout="wide")

# Título do aplicativo
st.markdown("<h1 style='text-align: center;'>📀 Cálculo do Desvio Padrão para Dados Agrupados</h1>", unsafe_allow_html=True)
st.write("Este aplicativo realiza o cálculo da variância e do desvio padrão para dados agrupados inseridos. Informe também se os dados são de uma amostra ou da população.")
st.write("---")

# Entrada para os dados
dados_input = st.sidebar.text_area("Insira os dados agrupados (valor:frequência) separados por vírgula:", value="1:2, 2:3, 3:5")
st.sidebar.write("Exemplo: 1:2, 2:3, 3:5")

# Tipo de dado: Amostra ou População
eh_amostra = st.sidebar.checkbox("Os dados correspondem a uma amostra?", value=False)

# Converter os dados de entrada em uma lista de tuplas (valor, frequência)
try:
    dados_input_split = re.split(r",\s*|\n\s*", dados_input.strip())
    dados_input_split = [x.strip() for x in dados_input_split if x.strip()]
    dados_agrupados = [tuple(map(float, item.split(':'))) for item in dados_input_split]

except ValueError:
    st.error("Por favor, insira os valores e frequências corretamente no formato valor:frequência, separados por vírgulas.")
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
        media = calcular_media(dados_agrupados)
        variancia, somatorio = calcular_variancia(dados_agrupados, media, eh_amostra)
        desvio_padrao = calcular_desvio_padrao(variancia)

        # Exibir os resultados
        st.write("## Cálculo:")
        dados_somatorio_str = ' + '.join([f'{valor} \\times {frequencia}' for valor, frequencia in dados_agrupados])
        dados_variancia_str = ' + '.join([f'({valor} - {round(media, 2)})^2 \\times {frequencia}' for valor, frequencia in dados_agrupados])

        st.latex(f"\\text{{Média}}: \\bar{{X}} = \\frac{{\\sum (x_i \\times f_i)}}{{\\sum f_i}} = \\frac{{{dados_somatorio_str}}}{{{total_frequencia}}} = {round(media, 2)}")
        st.latex(f"\\text{{Variância}}: s^2 = \\frac{{\\sum (x_i - \\bar{{X}})^2 \\times f_i}}{{{'n - 1' if eh_amostra else 'n'}}}")
        st.latex(f"\\sum (x_i - \\bar{{X}})^2 \\times f_i = {dados_variancia_str} = {round(somatorio, 3)}")
        st.latex(f"s^2 = \\frac{{{round(somatorio, 3)}}}{{{total_frequencia - 1 if eh_amostra else total_frequencia}}} = {round(variancia, 3)}")
        st.latex(f"\\text{{Desvio Padrão}}: s = \\sqrt{{s^2}} = \\sqrt{{{round(variancia, 3)}}} = {round(desvio_padrao, 3)}")
else:
    st.info("Aguardando o cálculo.")
