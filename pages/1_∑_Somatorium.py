import streamlit as st

st.set_page_config(page_title="Somatório de forma prática", page_icon="∑",layout="wide")

# Título do aplicativo
st.title("∑ Somatório de forma prática")
st.write("Este aplicativo realiza o cálculo do somatório de uma variável X, com base nos limites inferior e superior.")
st.write("---")

# Entrada para os dados (X)
st.sidebar.write("Insira os valores da variável X, separados por vírgulas:")
dados_input = st.sidebar.text_area("Exemplo: 1, 2, 3, 4, 5", value="1, 2, 3, 4, 5")

# Entrada para o limite inferior (LI)
i = st.sidebar.number_input("Informe o limite inferior (i ou LI):", min_value=1, value=1)

# Converter os dados de entrada em uma lista de floats
try:
    dados = list(map(float, dados_input.split(',')))
except ValueError:
    st.error("Por favor, insira os valores corretamente separados por vírgulas.")

# Entrada para o limite superior (LS) iniciando com o tamanho de X
n = st.sidebar.number_input("Informe o limite superior (n ou LS):", min_value=i, value=len(dados))


# Opções para o tipo de operação
operacao = st.sidebar.selectbox(
    "Selecione o tipo de operação:",
    ("Soma Simples", "Soma dos Quadrados", "Quadrado da Soma")
)

# Definir a função para o somatório
def somatorio(tipo_operacao, dados, i, n):
    if n > len(dados):
        st.error("O limite superior não pode ser maior que o tamanho da lista de dados.")
        return None, None

    if tipo_operacao == "Soma Simples":
        elementos = dados[i-1:n]  # Pegando os elementos entre os limites i e n
        soma = sum(elementos)
        expressao = " + ".join([f"{x}" for x in elementos])
        return soma, f"\\sum_{{i={i}}}^{{n={n}}} X_{{i}} = {expressao} = {soma}"

    elif tipo_operacao == "Soma dos Quadrados":
        elementos = dados[i-1:n]  # Pegando os elementos entre os limites i e n
        soma_quadrados = sum(x**2 for x in elementos)
        expressao = " + ".join([f"{x}^2" for x in elementos])
        return soma_quadrados, f"\\sum_{{i={i}}}^{{n={n}}} X^2_{{i}} = {expressao} = {soma_quadrados}"

    elif tipo_operacao == "Quadrado da Soma":
        elementos = dados[i-1:n]  # Pegando os elementos entre os limites i e n
        soma = sum(elementos)
        expressao = " + ".join([f"{x}" for x in elementos])
        return soma**2, f"\\left(\\sum_{{i={i}}}^{{n={n}}} X_{{i}} \\right)^2 = \\left({expressao}\\right)^2 = {soma**2}"

# Processar o somatório e exibir o resultado
if st.sidebar.button("Calcular Somatório"):
    resultado, expressao = somatorio(operacao, dados, i, n)
    
    if resultado is not None and expressao is not None:
        # Exibir a expressão do somatório usando símbolos matemáticos
        st.latex(expressao)
        
        # Exibir o resultado do somatório
        st.write(f"**Resultado do somatório**: {resultado}")
