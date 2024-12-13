import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configuração inicial
st.set_page_config(page_title="Sumarização de Dados", page_icon="⚙️", layout="wide")
st.title("📊 Sumarização de Dados a partir de Arquivos")

st.write("""
Faça upload de um arquivo (CSV, XLSX ou TSV) e explore as estatísticas descritivas dos dados, 
como média, desvio padrão, intervalos de confiança e gráficos interativos.
""")

# Função para calcular intervalo de confiança
def calc_confidence_interval(data, confidence=0.95):
    mean = np.mean(data)
    stderr = np.std(data, ddof=1) / np.sqrt(len(data))
    margin = stderr * stats.t.ppf((1 + confidence) / 2., len(data) - 1)
    return mean - margin, mean + margin

# Upload do arquivo
uploaded_file = st.file_uploader("Faça upload do seu arquivo (CSV, XLSX ou TSV)", type=["csv", "xlsx", "tsv"])

if uploaded_file:
    # Detectar tipo de arquivo e carregar os dados
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    elif uploaded_file.name.endswith(".tsv"):
        df = pd.read_csv(uploaded_file, sep="\t")

    # Remover a coluna "Semana" se existir
    if "Semana" in df.columns:
        df = df.drop(columns=["Semana"])

    st.write("---")
    st.write("### Prévia dos Dados 🗂️")
    st.dataframe(df.head())

    # Sumarização dos dados
    st.write("---")
    st.write("### Estatísticas Descritivas 📊")
    summary = df.describe().T
    summary = summary.round(1)  # Arredondar para uma casa decimal
    
    # Adicionar intervalo de confiança
    for confidence in [0.90, 0.95, 0.99]:
        lower_bounds = []
        upper_bounds = []
        for col in df.select_dtypes(include=[np.number]).columns:
            lb, ub = calc_confidence_interval(df[col].dropna(), confidence=confidence)
            lower_bounds.append(round(lb, 1))
            upper_bounds.append(round(ub, 1))
        summary[f"IC {int(confidence * 100)}% Inf"] = lower_bounds
        summary[f"IC {int(confidence * 100)}% Sup"] = upper_bounds

    st.dataframe(summary)

    # Gráficos
    st.write("---")
    st.write("### Visualização Gráfica 📈")

    # Boxplot combinado
    # st.write("#### Comparação de Todas as Colunas em um Único Boxplot")
    cols = df.select_dtypes(include=[np.number]).columns
    if len(cols) > 0:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=df[cols], ax=ax, palette="Set3")
        ax.set_title("Boxplot de Todas as Colunas Numéricas")
        ax.grid(True, linestyle='--', linewidth=0.5)
        st.pyplot(fig)

    if len(cols) > 0:
        st.write("---")
        st.write("#### Histogramas")
        # Configurar bins e limites globais
        global_min = df[cols].min().min()
        global_max = df[cols].max().max()
        bins = np.linspace(global_min, global_max, 20)
        fig, axes = plt.subplots(1, len(cols), figsize=(5 * len(cols), 5), sharey=True, sharex=True)
        if len(cols) == 1:
            axes = [axes]
        for ax, col in zip(axes, cols):
            sns.histplot(df[col], bins=bins, kde=True, ax=ax, color='skyblue', edgecolor='black')
            ax.set_title(f"Histograma de {col}")
            ax.grid(True, linestyle='--', linewidth=0.5)
        st.pyplot(fig)


    # Comparação do Volume Médio de Compras por Filial
    if len(df.columns) > 1:
        st.write("---")
        # st.write("#### Comparação do Volume Médio de Compras por Filial")
        media_por_filial = df.iloc[:,:].mean()
        fig, ax = plt.subplots(figsize=(10, 6))
        media_por_filial.plot(kind='bar', color='skyblue', edgecolor='black', ax=ax)
        ax.set_title("Comparação do Volume Médio de Compras por Filial")
        ax.set_xlabel("Filial")
        ax.set_ylabel("Volume Médio de Compras")
        ax.grid(True, linestyle='--', linewidth=0.5)
        st.pyplot(fig)

    # Correlação Entre Filiais
    if len(df.columns) > 1:
        st.write("---")
        # st.write("#### Correlação Entre Filiais")
        correlation_matrix = df.iloc[:,:].corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
        ax.set_title("Correlação Entre Volumes de Compras das Filiais")
        st.pyplot(fig)

    # Análise de Sazonalidade
    if "Semana" in df.columns:
        st.write("---")
        # st.write("#### Análise de Sazonalidade")
        pivot_data = df.set_index("Semana").T
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(pivot_data, cmap='YlGnBu', cbar=True, annot=False, ax=ax)
        ax.set_title("Sazonalidade de Compras ao Longo das Semanas")
        ax.set_xlabel("Semana")
        ax.set_ylabel("Filial")
        st.pyplot(fig)

    # Ranking de Filiais por Total de Compras no Ano
    if len(df.columns) > 1:
        st.write("---")
        # st.write("#### Ranking de Filiais por Total de Compras no Ano")
        total_por_filial = df.iloc[:,:].sum()
        fig, ax = plt.subplots(figsize=(10, 6))
        total_por_filial.sort_values().plot(kind='barh', color='salmon', edgecolor='black', ax=ax)
        ax.set_title("Ranking de Filiais por Total de Compras no Ano")
        ax.set_xlabel("Volume Total de Compras")
        ax.set_ylabel("Filial")
        ax.grid(True, linestyle='--', linewidth=0.5)
        st.pyplot(fig)




    # Adicionando teste de hipóteses
    st.write("---")
    st.write("### Teste de Hipóteses 📊")
    st.write("""
    Realize um teste t de Student para comparar as médias de duas colunas numéricas no conjunto de dados. 
    O teste verifica se há diferença significativa entre as médias das colunas selecionadas.
    """)

    # Selecionar as colunas numéricas
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()

    if len(numeric_columns) >= 2:
        col1 = st.selectbox("Selecione a primeira coluna:", numeric_columns, key="col1")
        col2 = st.selectbox("Selecione a segunda coluna:", numeric_columns, key="col2")
        alpha = st.slider("Escolha o nível de significância (α):", 0.01, 0.10, 0.05, key="alpha")
        
        if st.button("Executar Teste de Hipóteses"):
            # Dados das colunas selecionadas
            data1 = df[col1].dropna()
            data2 = df[col2].dropna()
            
            # Realizar o teste t de Student
            t_stat, p_value = stats.ttest_ind(data1, data2, equal_var=False)
            
            # Exibir resultados
            st.write("#### Resultado do Teste de Hipóteses")
            result_df = pd.DataFrame({
                "Estatística t": [t_stat],
                "p-valor": [p_value],
                "Conclusão": ["Rejeitamos H0" if p_value < alpha else "Não rejeitamos H0"],
                "Explicação" : ["Há diferença significativa entre as médias" if p_value < alpha else "Não há diferença significativa entre as médias"]
            })
            st.table(result_df)
            
            # Visualizar os dados
            st.write("### Visualização Gráfica 📈")
            # Gráfico de barras com médias e intervalos de confiança
            means = [np.mean(data1), np.mean(data2)]
            std_errors = [
                np.std(data1, ddof=1) / np.sqrt(len(data1)),
                np.std(data2, ddof=1) / np.sqrt(len(data2))
            ]
            
            fig, ax = plt.subplots()
            bars = ax.bar([col1, col2], means, yerr=std_errors, capsize=10, color=["blue", "green"])
            ax.set_title("Médias com Intervalos de Confiança")
            ax.set_ylabel("Média")
            ax.grid(axis="y", linestyle="--", alpha=0.6)
            st.pyplot(fig)
    else:
        st.info("Por favor, selecione ao menos duas colunas numéricas para realizar o teste de hipóteses.")




else:
    st.info("Por favor, faça upload de um arquivo para começar.")