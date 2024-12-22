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
confidence_level = st.selectbox("Escolha o nível de confiança (%)", [90, 95, 99])

# Botão para calcular o intervalo de confiança
if st.button("Calcular IC"):
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

    st.write(f"Este intervalo de confiança significa que estamos {confidence_level}% confiantes de que a média verdadeira da população está entre os limites calculados.")
    # Explicação divertida sobre intervalo de confiança
    st.write("### Explicação Divertida do Intervalo de Confiança")
    st.write(
        f"Imagine que você está jogando bolinhas de papel em uma lixeira do outro lado da sala. A lixeira é o alvo e você quer saber se a maioria das bolinhas vai cair dentro dela ou não. O intervalo de confiança é como uma zona imaginária ao redor da lixeira, que diz: 'Olha, eu não sei exatamente onde cada bolinha vai cair, mas estou {confidence_level}% confiante de que a maioria das bolinhas vai parar dentro dessa área!'. Quanto mais confiante você quer estar, maior você precisa fazer essa zona. Então, o intervalo de confiança é a sua maneira de garantir, com certa margem de segurança, que a maioria dos arremessos está na direção certa."
    )

    # Análise visual dos resultados
    fig, ax = plt.subplots()
    ax.axvline(lower_bound, color='red', linestyle='--', label='Limite Inferior')
    ax.axvline(upper_bound, color='red', linestyle='--', label='Limite Superior')
    ax.axvline(mean, color='blue', linestyle='-', label='Média da Amostra')
    ax.fill_betweenx([0, 1], lower_bound, upper_bound, color='red', alpha=0.4)
    ax.set_xlabel('Valor')
    ax.set_yticks([])
    ax.set_title(f"Intervalo de Confiança de {confidence_level}%")
    ax.legend()

    st.pyplot(fig)
else:
    st.info("Aguardando o cálculo do intervalo de confiança.")