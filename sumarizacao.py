import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Título do aplicativo
st.title("Sumarização de dados")

# Entrada dos dados
st.sidebar.write("# Entre com os dados")
st.sidebar.write("Insira os dados separados por vírgulas:")
dados_input = st.sidebar.text_area("Exemplo: 6.67, 6.82, 6.90, 7.05, 7.10")

# Converter a string de entrada em uma lista de floats
if dados_input:
    try:
        # Converter os dados para uma lista de floats
        dados = list(map(float, dados_input.split(',')))
        
        # Converter para DataFrame para manipulações
        df = pd.DataFrame(dados, columns=["Valores"])

        # Sumarização dos dados
        n = len(dados)
        media = np.mean(dados)
        mediana = np.median(dados)
        moda_result = stats.mode(dados, keepdims=True)
        moda = moda_result.mode[0]  # Pegar o primeiro valor da moda
        quartis = np.percentile(dados, [25, 50, 75])
        valor_min = np.min(dados)
        valor_max = np.max(dados)
        desvio_padrao = np.std(dados)  # Desvio padrão
        variancia = np.var(dados)  # Variância
        
        # Exibir sumarização
        st.write("### Sumarização dos Dados:")
        st.write(f"**Tamanho da amostra**: {n}")
        st.write(f"**Média**: {media}")
        st.write(f"**Mediana**: {mediana}")
        st.write(f"**Moda**: {moda}")
        st.write(f"**1º Quartil (Q1)**: {quartis[0]}")
        st.write(f"**2º Quartil (Mediana/Q2)**: {quartis[1]}")
        st.write(f"**3º Quartil (Q3)**: {quartis[2]}")
        st.write(f"**Mínimo**: {valor_min}")
        st.write(f"**Máximo**: {valor_max}")
        st.write(f"**Desvio Padrão**: {desvio_padrao}")
        st.write(f"**Variância**: {variancia}")
        
        # Gerar o histograma
        st.write("### Histograma dos Dados:")
        fig, ax = plt.subplots()
        ax.hist(dados, bins=10, edgecolor='black')
        ax.set_xlabel('Faixas de Valores')
        ax.set_ylabel('Frequência')
        
        # Exibir o histograma
        st.pyplot(fig)
    
    except ValueError:
        st.error("Por favor, insira os dados corretamente no formato numérico, separados por vírgula.")
else:
    st.info("Aguardando a entrada dos dados.")
