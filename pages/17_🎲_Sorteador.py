import streamlit as st
import pandas as pd
import random

# Configuração da página
st.set_page_config(page_title="Sorteio de Nomes", page_icon="🎲", layout="wide")
st.markdown("<h1 style='text-align: center;'>🎲 Sorteio Aleatório de Nomes</h1>", unsafe_allow_html=True)
st.write("Este aplicativo realiza o sorteio de nomes a partir de um arquivo carregado ou inseridos manualmente.")
st.write("---")

# Função para carregar os dados
@st.cache_data
def load_data(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file, header=None)
    elif file.name.endswith(".xlsx"):
        return pd.read_excel(file, header=None)
    elif file.name.endswith(".txt"):
        return pd.read_csv(file, header=None) 
    else:
        st.error("Formato de arquivo não suportado. Por favor, envie um arquivo .csv, .xlsx ou .txt.")
        return None

# Opção de inserir nomes manualmente
option = st.radio("Como você deseja fornecer os nomes?", ("Upload de Arquivo", "Inserir Manualmente"))

df = None

if option == "Upload de Arquivo":
    # Carregar o arquivo
    uploaded_file = st.file_uploader("Faça upload do seu arquivo (CSV, XLSX ou TXT)", type=["csv", "xlsx", "txt"])

    if uploaded_file:
        # Exibir os dados carregados
        df = load_data(uploaded_file)
        st.write("### Lista de Nomes Carregados:")
        st.dataframe(df)

elif option == "Inserir Manualmente":
    names_input = st.text_area("Digite os nomes, um por linha:")
    if names_input:
        names_list = names_input.strip().split("\n")
        df = pd.DataFrame(names_list)
        st.write("### Lista de Nomes Inseridos:")
        st.dataframe(df)

if df is not None and not df.empty:
    # Escolher quantidade de sorteados
    num_sorteados = st.slider("Quantos nomes deseja sortear?", min_value=1, max_value=len(df), value=1)

    # Realizar o sorteio
    if st.button("Sortear"):
        sorteados = random.sample(df[0].tolist(), num_sorteados)
        resultado_df = pd.DataFrame(sorteados, columns=["Sorteados"])

        st.write("### Resultado do Sorteio:")
        st.dataframe(resultado_df)
else:
    st.info("Por favor, forneça os nomes para realizar o sorteio.")
