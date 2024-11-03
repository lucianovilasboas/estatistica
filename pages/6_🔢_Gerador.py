import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Título da aplicação
st.title("Gerador de Dados Sintéticos")

# Parâmetros de entrada do usuário
mean = st.sidebar.number_input("Média:", value=0.0)
std_dev = st.sidebar.number_input("Desvio Padrão:", value=1.0)
size = st.sidebar.number_input("Tamanho do Conjunto de Dados:", min_value=1, value=100, step=1)

# Botão para gerar os dados
if st.sidebar.button("Gerar Dados"):
    # Gerando o conjunto de dados sintético
    data = np.random.normal(loc=mean, scale=std_dev, size=size)
    data = np.round(data, 2)
    df = pd.DataFrame(data, columns=["Valor"])

    # Mostrando o conjunto de dados
    # st.write("Conjunto de Dados Sintético:")
    # st.write(df)

    # Exibindo os dados em uma área de texto
    st.write("Dados Gerados:")
    st.text_area("Valores:", ", ".join(map(str, data)), height=200)

    # Criando um histograma com distribuição normal
    st.write("### Histograma dos Dados (Distribuição Aproximada)")
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, density=True, alpha=0.6, color='blue', edgecolor='black')
    
    # Linhas para a curva da distribuição normal
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, size)
    y = (1 / (np.sqrt(2 * np.pi * std_dev**2))) * np.exp(-0.5 * ((x - mean) / std_dev)**2)
    ax.plot(x, y, 'r--', label="Distribuição Normal")
    
    ax.set_xlabel("Valor")
    ax.set_ylabel("Densidade")
    ax.legend()
    st.pyplot(fig)

    # Download do conjunto de dados
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Baixar Conjunto de Dados como CSV",
        data=csv,
        file_name='dados_sinteticos.csv',
        mime='text/csv',
    )
else:
    st.info("Aguardando a geração dos dados.")