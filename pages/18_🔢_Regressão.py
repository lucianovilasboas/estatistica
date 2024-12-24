import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Configuracao inicial
st.set_page_config(page_title="Regressão Linear", page_icon="🔢", layout="wide")
st.title("🔢 Regressão Linear com Dados Informados ou Importados")

st.write("""
🔍 **Carregue seus dados** ou ✏️ insira manualmente para realizar uma **regressão linear simples** e visualizar os resultados.

### 📥 Entrada
- Valores **X** e **Y**
- Arquivos nos formatos **CSV**, **XLSX** ou **TSV**

### 📊 Saída
- **Equação da reta**
- **Coeficiente de determinação** ($R^2$)
- **Gráfico visual**
- **Exportação de resultados** em **CSV**

---
""")

# Função para carregar os dados
def carregar_dados(arquivo):
    if arquivo.name.endswith(".csv"):
        return pd.read_csv(arquivo)
    elif arquivo.name.endswith(".xlsx"):
        return pd.read_excel(arquivo)
    elif arquivo.name.endswith(".tsv"):
        return pd.read_csv(arquivo, sep="\t")
    return None

# Sidebar para upload de arquivo
uploaded_file = st.sidebar.file_uploader("📥 Carregue um arquivo (CSV, XLSX, TSV)", type=["csv", "xlsx", "tsv"])

# Entrada manual dos dados
st.sidebar.write("✏️ Ou insira os dados manualmente")

x_sample = ",".join(map(str,[-49, 39, -34, -18, -42, -8, -3, -12, 42, -9, -25, 48, -1, -26, -27, -38, 9, -44, 6, -15, -6, -31, 14, -43, -35, -37, 25, 36, -36, 41, 47, 15, -19, 36, 12, 35, 0, -26, 7, 12, 11, -29, 7, 7, 35, -2, 1, -9, 19, -36]))
y_sample = ",".join(map(str,[-18, 15, -14, -5, -25, -4, -17, -11, 19, -10, -4, 16, -2, -12, -6, -26, 10, -21, -1, -5, -2, -18, 7, -23, -16, -15, 20, 11, -7, 10, 22, 10, -8, 14, 4, 15, -2, -8, 5, 2, 9, -12, 7, 6, 13, -3, 4, -1, 9, -17]))

x_input = st.sidebar.text_area("🔢 Valores de X (separados por vírgulas)", value=x_sample)
y_input = st.sidebar.text_area("🔢 Valores de Y (separados por vírgulas)", value=y_sample)

# Carregar ou processar dados
if uploaded_file:
    df = carregar_dados(uploaded_file)
    if df is not None:
        st.write("### 📄 Dados Importados")
        st.dataframe(df)
        if df.shape[1] >= 2:
            X = df.iloc[:, [0]].values  # Primeira coluna como X
            y = df.iloc[:, 1].values    # Segunda coluna como Y
        else:
            st.error("⚠️ O arquivo deve conter pelo menos duas colunas.")
else:
    try:
        X = np.array([float(i) for i in x_input.split(',')]).reshape(-1, 1)
        y = np.array([float(i) for i in y_input.split(',')])
        if len(X) != len(y):
            st.error("⚠️ As listas de X e Y devem ter o mesmo tamanho.")
            st.stop()
    except ValueError:
        st.error("⚠️ Certifique-se de inserir apenas números separados por vírgulas.")
        st.stop()

# Modelo de regressão linear
if st.button("⚙️ Calcular Regressão Linear"):
    model = LinearRegression()
    model.fit(X, y)

    # Predicao
    y_pred = model.predict(X)

    # Coeficientes
    coeficiente = model.coef_[0]
    intercepto = model.intercept_
    r2 = r2_score(y, y_pred)
    rmse = mean_squared_error(y, y_pred) 

    st.write("## 📊 Resultados da Regressão Linear")
    st.write("**🧮 Equação da Reta:**")
    st.latex(r"y = %.2f x %s %.2f" % (coeficiente, "+" if intercepto >= 0 else "" , intercepto))
    st.write(f"**📈 R² (Coeficiente de Determinação):** {r2:.4f}")
    st.write(f"**📉 Erro Quadrático Médio (RMSE):** {rmse:.4f}")

    # Gráfico
    st.write("## 📈 Gráfico da Regressão Linear")
    fig, ax = plt.subplots()
    ax.scatter(X, y, color='blue', label='Dados reais', alpha=0.5)
    ax.plot(X, y_pred, color='red', linewidth=2, label='Reta Ajustada', alpha=0.3)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    ax.grid()
    st.pyplot(fig)

    # Exportar os resultados
    if st.checkbox("💾 Exportar Resultados"):
        result_df = pd.DataFrame({
            'X': X.flatten(),
            'Y Real': y,
            'Y Predito': y_pred
        })
        st.write("### 📄 Resultados Exportáveis")
        st.dataframe(result_df)

        csv = result_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="💾 Baixar Resultados como CSV",
            data=csv,
            file_name="resultados_regressao_linear.csv",
            mime="text/csv",
        )
else:
    st.info("ℹ️ Clique no botão para calcular a regressão linear.")
