import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

st.set_page_config(layout="wide")

# Título do aplicativo
st.title("Geração de Distribuições")

# Entradas para gerar uma distribuição normal
st.sidebar.write("# Forneça parâmetros para gerar distribuição normal")
media_input = st.sidebar.number_input("Média", value=0.0)
desvio_padrao_input = st.sidebar.number_input("Desvio Padrão", value=1.0)
tamanho_amostra_input = st.sidebar.number_input("Tamanho da Amostra", value=100, step=1)

# Botão para gerar a distribuição
gerar_distribuicao = st.sidebar.button("Gerar Distribuição Normal")

# Gerar distribuição normal baseada em média e desvio padrão fornecidos
if gerar_distribuicao:
    try:
        # Gerar dados de uma distribuição normal
        dados_gerados = np.random.normal(loc=media_input, scale=desvio_padrao_input, size=tamanho_amostra_input)
        
        # Converter para DataFrame para manipulações
        df_gerados = pd.DataFrame(dados_gerados, columns=["Valores Gerados"])

        # Exibir os dados gerados
        st.write("### Dados Gerados:")
        st.write(df_gerados)

        # Sumarização dos dados gerados
        n_gerados = len(dados_gerados)
        media_gerados = np.mean(dados_gerados)
        mediana_gerados = np.median(dados_gerados)
        moda_result_gerados = stats.mode(dados_gerados, keepdims=True)
        moda_gerados = moda_result_gerados.mode[0]  # Pegar o primeiro valor da moda
        quartis_gerados = np.percentile(dados_gerados, [25, 50, 75])
        valor_min_gerados = np.min(dados_gerados)
        valor_max_gerados = np.max(dados_gerados)
        desvio_padrao_gerados = np.std(dados_gerados)  # Desvio padrão
        variancia_gerados = np.var(dados_gerados)  # Variância
        
        # Exibir sumarização dos dados gerados
        st.write("### Sumarização dos Dados Gerados:")
        st.write(f"**Tamanho da amostra**: {n_gerados}")
        st.write(f"**Média**: {media_gerados}")
        st.write(f"**Mediana**: {mediana_gerados}")
        st.write(f"**Moda**: {moda_gerados}")
        st.write(f"**1º Quartil (Q1)**: {quartis_gerados[0]}")
        st.write(f"**2º Quartil (Mediana/Q2)**: {quartis_gerados[1]}")
        st.write(f"**3º Quartil (Q3)**: {quartis_gerados[2]}")
        st.write(f"**Mínimo**: {valor_min_gerados}")
        st.write(f"**Máximo**: {valor_max_gerados}")
        st.write(f"**Desvio Padrão**: {desvio_padrao_gerados}")
        st.write(f"**Variância**: {variancia_gerados}")
        
        # Gerar o histograma dos dados gerados
        st.write("### Histograma dos Dados Gerados:")
        fig_gerados, ax_gerados = plt.subplots()
        ax_gerados.hist(dados_gerados, bins=10, edgecolor='black')
        ax_gerados.set_xlabel('Faixas de Valores Gerados')
        ax_gerados.set_ylabel('Frequência')
        
        # Exibir o histograma dos dados gerados
        st.pyplot(fig_gerados)
    
    except ValueError:
        st.error("Erro ao gerar a distribuição normal. Verifique os parâmetros fornecidos.")

else:
    st.info("Aguardando a geração de distribuição.")
