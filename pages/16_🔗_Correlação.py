import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Configuração da página
st.set_page_config(page_title="Cálculo de Correlação", page_icon="🔗", layout="wide")
st.markdown("<h1 style='text-align: center;'>🔗 Cálculo de Correlação</h1>", unsafe_allow_html=True)
st.write("Este aplicativo permite calcular correlações entre colunas de um arquivo de dados carregado e gerar gráficos.")
st.write("---")

# Exibir a fórmula da correlação
st.markdown("### Fórmula da Correlação")
st.latex(r"""r = \frac{n(\Sigma xy) - (\Sigma x)(\Sigma y)}{\sqrt{[n\Sigma x^2 - (\Sigma x)^2][n\Sigma y^2 - (\Sigma y)^2]}}""")
st.write("---")

# Função para carregar os dados
@st.cache_data
def load_data(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    elif file.name.endswith(".xlsx"):
        return pd.read_excel(file)
    else:
        st.error("Formato de arquivo não suportado. Por favor, envie um arquivo .csv ou .xlsx.")
        return None

# Carregar o arquivo
uploaded_file = st.file_uploader("Faça upload do seu arquivo (CSV ou XLSX)", type=["csv", "xlsx"])

if uploaded_file:
    # Exibir os dados
    df = load_data(uploaded_file)
    st.write("### Visualização dos Dados:")
    st.dataframe(df)

    # Calcular a matriz de correlação
    st.write("---")
    st.write("### Matriz de Correlação 📊")
    correlation_matrix = df.corr()
    st.dataframe(correlation_matrix)

    # Visualizar a matriz de correlação como um mapa de calor
    st.write("### Mapa de Calor da Correlação")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    ax.set_title("Mapa de Calor da Correlação")
    st.pyplot(fig)

    # Selecionar colunas para gráfico de dispersão
    st.write("---")
    st.write("### Gráfico de Correlação entre Duas Colunas")
    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()

    if len(numeric_columns) < 2:
        st.warning("O arquivo deve conter ao menos duas colunas numéricas para criar um gráfico de correlação.")
    else:
        col1 = st.selectbox("Selecione a primeira coluna:", numeric_columns, key="col1")
        col2 = st.selectbox("Selecione a segunda coluna:", numeric_columns, key="col2")

        raio = 100
        max = np.maximum(df[col1].values.max(), df[col1].values.max())
        area_x = df[col1].values * raio / max
        area_y = df[col1].values * raio / max

        if col1 and col2:
            st.write(f"### Gráfico de Dispersão: {col1} vs {col2}")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.scatterplot(x=df[col1], y=df[col2],ax=ax, color="blue", alpha=0.4, edgecolor="k", s=area_x+area_y)

            # Adicionar a reta de ajuste
            X = df[col1].values.reshape(-1, 1)
            y = df[col2].values
            model = LinearRegression()
            model.fit(X, y)
            y_pred = model.predict(X)
            ax.plot(df[col1], y_pred, color="red", linewidth=1, label="Reta de Ajuste")
            ax.legend()

            ax.set_xlabel(col1)
            ax.set_ylabel(col2)
            ax.set_title(f"Correlação: {correlation_matrix.loc[col1, col2]:.2f}")
            st.pyplot(fig)
else:
    st.info("Por favor, faça upload de um arquivo para começar.")
