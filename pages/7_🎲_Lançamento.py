import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

# Interface do Streamlit
st.set_page_config(page_title="Simulação de Lançamento", page_icon="🎲")

st.markdown("<h1 style='text-align: center;'>🎲 Simulação de Lançamento</h1>", unsafe_allow_html=True)
st.write("Este aplicativo simula o lançamento de um dado ou uma moeda.")


# Função para simular lançamentos de dados
def simulate_dice_rolls(n):
    rolls = [random.randint(1, 6) for _ in range(n)]
    roll_counts = {face: rolls.count(face) for face in range(1, 7)}
    return pd.DataFrame(list(roll_counts.items()), columns=["Face", "Count"])

# Função para simular lançamentos de moeda
def simulate_coin_flips(n):
    flips = [random.choice(["Cara", "Coroa"]) for _ in range(n)]
    flip_counts = {"Cara": flips.count("Cara"), "Coroa": flips.count("Coroa")}
    return pd.DataFrame(list(flip_counts.items()), columns=["Resultado", "Count"])


# Escolha entre dado ou moeda
choice = st.sidebar.selectbox("Escolha o que deseja lançar:", ["Dado", "Moeda"])

# Entrada do usuário para o número de lançamentos
n = st.sidebar.number_input("Número de lançamentos", min_value=1, step=1, value=100)

# Botão para iniciar a simulação
if st.sidebar.button("Lançar!"):
    if choice == "Dado":
        # Simular lançamentos de dado
        results_df = simulate_dice_rolls(n)
        st.write("Resultados dos lançamentos de dado:")
        st.dataframe(results_df)

        # Gráfico de barras dos resultados do dado
        fig, ax = plt.subplots()
        ax.bar(results_df["Face"], results_df["Count"])
        ax.set_xlabel("Face do Dado")
        ax.set_ylabel("Frequência")
        ax.set_title("Distribuição dos Resultados dos Lançamentos de Dado")
        st.pyplot(fig)
        
    elif choice == "Moeda":
        # Simular lançamentos de moeda
        results_df = simulate_coin_flips(n)
        st.write("Resultados dos lançamentos de moeda:")
        st.dataframe(results_df)

        # Gráfico de barras dos resultados da moeda
        fig, ax = plt.subplots()
        ax.bar(results_df["Resultado"], results_df["Count"])
        ax.set_xlabel("Resultado")
        ax.set_ylabel("Frequência")
        ax.set_title("Distribuição dos Resultados dos Lançamentos de Moeda")
        st.pyplot(fig)
else:
    st.info("Aguardando o lançamento.")