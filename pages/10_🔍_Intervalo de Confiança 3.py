import streamlit as st
import scipy.stats as stats
import math
import matplotlib.pyplot as plt

# Configurações da página
st.set_page_config(page_title="Calculadora de Intervalo de Confiança", page_icon="🔍")
# Título da página
st.title("🔍 Calculadora de Intervalo de Confiança (IC)")
st.write("Este aplicativo calcula o intervalo de confiança para uma média com base nos parâmetros fornecidos.")
st.write("---")

# Entrada de dados do usuário
mean = st.number_input("Digite a média da amostra (μ)", value=50.0)
std_dev = st.number_input("Digite o desvio padrão da amostra (s)", value=10.0, min_value=0.0)
sample_size = st.number_input("Digite o tamanho da amostra (n)", min_value=1, value=30, step=1)
confidence_levels = []

# Checkboxes para selecionar níveis de confiança
st.write("Escolha os níveis de confiança (%)")
if st.checkbox("90%", value=True):
    confidence_levels.append(90)
if st.checkbox("95%", value=True):
    confidence_levels.append(95)
if st.checkbox("99%", value=True):
    confidence_levels.append(99)

# Botão para calcular o intervalo de confiança
if st.button("Calcular IC"):
    # Configuração do gráfico
    fig, ax = plt.subplots()

    for confidence_level in confidence_levels:
        # Cálculo do valor crítico z com base no nível de confiança
        alpha = 1 - (confidence_level / 100)
        z_value = stats.norm.ppf(1 - alpha / 2)

        # Cálculo do erro padrão da média (EPM)
        standard_error = std_dev / math.sqrt(sample_size)

        # Cálculo da margem de erro (ME)
        margin_of_error = z_value * standard_error

        # Cálculo do intervalo de confiança
        lower_bound = mean - margin_of_error
        upper_bound = mean + margin_of_error

        # Exibir os resultados
        st.write(f"### Intervalo de Confiança de {confidence_level}%")
        st.write(f"- Limite Inferior: {lower_bound:.2f}")
        st.write(f"- Limite Superior: {upper_bound:.2f}")

        # Definir a cor com base no nível de confiança
        if confidence_level == 90:
            color = 'blue'
        elif confidence_level == 95:
            color = 'red'
        elif confidence_level == 99:
            color = 'green'

        # Adicionar ao gráfico
        ax.axvline(lower_bound, linestyle='--', color=color, label=f'Limite Inferior {confidence_level}%')
        ax.axvline(upper_bound, linestyle='--', color=color, label=f'Limite Superior {confidence_level}%')
        ax.fill_betweenx([0, 1], lower_bound, upper_bound, color=color, alpha=0.2, label=f'IC {confidence_level}%')

    # Configurações do gráfico
    ax.axvline(mean, color='black', linestyle='-', label='Média da Amostra')
    ax.set_xlabel('Valor')
    ax.set_yticks([])
    ax.set_title("Intervalos de Confiança")
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=1) 

    st.pyplot(fig)
else:
    st.info("Aguardando o cálculo do intervalo de confiança.")
