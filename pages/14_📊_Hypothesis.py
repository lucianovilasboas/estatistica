import streamlit as st
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# Configuração inicial da página
st.set_page_config(page_title="Teste de Hipóteses", page_icon="📊", layout="wide")
st.title("📊 Teste de Hipóteses entre Duas Amostras")
st.write("""
Bem-vindo ao teste de hipóteses! 🎉  
Compare duas amostras (ou populações) e visualize as diferenças/semelhanças em gráficos interativos. 
Vamos analisar se há uma diferença significativa entre elas! 🚀
""")

# Passo 1: Entrada de dados
st.header("1️⃣ Insira as duas amostras 📂")
sample1 = st.text_area("📈 Digite os valores da primeira amostra (separe por vírgulas)", "10, 12, 15, 14, 13")
sample2 = st.text_area("📉 Digite os valores da segunda amostra (separe por vírgulas)", "8, 9, 11, 10, 7")

# Converter as entradas para listas numéricas
try:
    data1 = np.array([float(x) for x in sample1.split(",")])
    data2 = np.array([float(x) for x in sample2.split(",")])
    valid_data = True
except ValueError:
    st.error("⚠️ Certifique-se de inserir apenas números separados por vírgulas.")
    valid_data = False

# Passo 2: Seleção de tipo de teste
if valid_data:
    st.header("2️⃣ Escolha o tipo de teste de hipótese ⚖️")
    test_type = st.selectbox("Selecione o teste desejado:", ["Teste t de Student", "Teste de Mann-Whitney U"])

    st.write("""
    ### Hipóteses
    - **H0**: Não há diferença significativa entre as médias das duas amostras.
    - **H1**: Há diferença significativa entre as médias das duas amostras.
    """)

    # Passo 3: Nível de significância
    st.header("3️⃣ Escolha o nível de significância 🔍")
    alpha = st.slider("Selecione o valor de alfa (nível de significância):", 0.01, 0.10, 0.05)

    # Passo 4: Realizar o teste de hipótese
    st.header("4️⃣ Resultado do teste 📊")
    if st.button("Calcular"):
        if test_type == "Teste t de Student":
            # Teste t para amostras independentes
            t_stat, p_value = stats.ttest_ind(data1, data2, equal_var=False)
            stat_name = "Estatística t"
        elif test_type == "Teste de Mann-Whitney U":
            # Teste não paramétrico Mann-Whitney
            t_stat, p_value = stats.mannwhitneyu(data1, data2, alternative='two-sided')
            stat_name = "Estatística U"

        # Exibir resultados
        st.success("✅ Resultado do Teste")
        st.write(f"**{stat_name}:** {t_stat:.4f}")
        st.write(f"**p-valor:** {p_value:.4f}")

        # Passo 5: Interpretação
        st.header("5️⃣ Conclusão 🧠")
        if p_value < alpha:
            st.write(f"#### 🎉 Como o p-valor ({p_value:.4f}) é menor que α ({alpha}), rejeitamos H0.")
            st.write("##### ➡️ **Há diferença significativa entre as amostras.**")
        else:
            st.write(f"#### 😌 Como o p-valor ({p_value:.4f}) é maior ou igual a α ({alpha}), não rejeitamos H0.")
            st.write("##### ➡️ **Não há diferença significativa entre as amostras.**")

        # Passo 6: Visualizar os dados
        st.header("6️⃣ Visualização Gráfica 📊")

        # Gráfico de boxplot para distribuição das amostras
        st.write("### Distribuição das Amostras 🧮")
        fig, ax = plt.subplots()
        ax.boxplot([data1, data2], labels=["Amostra 1", "Amostra 2"], patch_artist=True)
        ax.set_title("Distribuição das Amostras")
        ax.set_ylabel("Valores")
        st.pyplot(fig)

        # Gráfico de barras com intervalos de confiança
        st.write("### Comparação de Médias com Intervalos de Confiança 📊")
        means = [np.mean(data1), np.mean(data2)]
        std_errors = [np.std(data1, ddof=1) / np.sqrt(len(data1)), np.std(data2, ddof=1) / np.sqrt(len(data2))]

        fig, ax = plt.subplots()
        bars = ax.bar(["Amostra 1", "Amostra 2"], means, yerr=std_errors, capsize=10, color=["blue", "green"])
        ax.set_ylabel("Média")
        ax.set_title("Média das Amostras com Intervalos de Confiança")
        ax.grid(axis='y', linestyle='--', alpha=0.6)
        st.pyplot(fig)

# Passo 7: Explicação adicional
st.header("ℹ️ Explicação")
st.write("""
Os testes realizados têm as seguintes características:  
- **Teste t de Student**: Comparação de médias assumindo distribuições normais.  
- **Teste de Mann-Whitney U**: Teste não paramétrico para comparar distribuições sem assumir normalidade.  

Os gráficos ajudam a visualizar as diferenças ou similaridades entre as duas amostras.  
O gráfico de barras inclui intervalos de confiança calculados a partir do erro padrão da média. 🎨
""")
