import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Título da aplicação
st.set_page_config(page_title="Gerador de Dados Sintéticos", page_icon="🔢")
# Alinhar o título da página ao centro
st.markdown("<h1 style='text-align: center;'>🔢 Gerador de Dados Sintéticos</h1>", unsafe_allow_html=True)
st.write("Este aplicativo gera um conjunto de dados sintéticos com base nos parâmetros fornecidos pelo usuário.")
st.write("---")
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

    # Layout para imagem e texto ao lado
    col1, col2 = st.columns([2, 4])
    with col1:
        # Exibindo os dados em uma área de texto
        st.markdown("<h4 style='text-align: center;'>Dados Gerados</h4>", unsafe_allow_html=True)
        
        st.text_area("Valores:", ", ".join(map(str, data)), height=200)

        # Download do conjunto de dados
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Baixar Conjunto de Dados como CSV",
            data=csv,
            file_name='dados_sinteticos.csv',
            mime='text/csv',
        )        

    with col2:
        # Criando um histograma com distribuição normal
        st.markdown("<h4 style='text-align: center;'>Histograma dos Dados (Distribuição Aproximada)</h4>", unsafe_allow_html=True)
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


else:
    st.info("Aguardando a geração dos dados.")