import streamlit as st

# Título do aplicativo
st.title("Somatório de forma prática") 

# Entrada para os dados (X)
st.write("Insira os valores da variável X, separados por vírgulas:")
dados_input_X = st.text_area("Exemplo para X: 1, 2, 3, 4, 5", value="1, 2, 3, 4, 5")

# Entrada para os dados (Y)
st.write("Insira os valores da variável Y, separados por vírgulas (mesmo tamanho que X):")
dados_input_Y = st.text_area("Exemplo para Y: 5, 4, 3, 2, 1", value="5, 4, 3, 2, 1")

# Entrada para o limite inferior (LI)
i = st.number_input("Informe o limite inferior (i ou LI):", min_value=1, value=1)

# Converter os dados de entrada em uma lista de floats
try:
    dados_X = list(map(float, dados_input_X.split(',')))
    dados_Y = list(map(float, dados_input_Y.split(',')))
except ValueError:
    st.error("Por favor, insira os valores corretamente separados por vírgulas.")

# Verificar se o tamanho das listas de X e Y é o mesmo
if len(dados_X) != len(dados_Y):
    st.error("As listas de X e Y precisam ter o mesmo tamanho.")

# Entrada para o limite superior (LS) iniciando com o tamanho de X
n = st.number_input("Informe o limite superior (n ou LS):", min_value=i, value=len(dados_X))

# Seletor para escolher se as operações serão feitas em X ou Y
variavel = st.selectbox("Selecione a variável para aplicar as operações:", ("X", "Y"))

# Opções para o tipo de operação
operacao = st.selectbox(
    "Selecione o tipo de operação:",
    ("Soma Simples (X ou Y)", "Soma dos Quadrados (X ou Y)", "Quadrado da Soma (X ou Y)", 
     "Soma de Produtos (X e Y)", "Produto da Soma (X e Y)", "Produto da Soma de Quadrados (X e Y)", 
     "Soma de Quadrados de Produtos (X e Y)")
)

# Definir a função para o somatório
def somatorio(tipo_operacao, dados, dados_X, dados_Y, i, n):
    if n > len(dados_X) or n > len(dados_Y):
        st.error("O limite superior não pode ser maior que o tamanho da lista de dados.")
        return None, None

    if tipo_operacao == "Soma Simples (X ou Y)":
        elementos = dados[i-1:n]  # Pegando os elementos entre os limites i e n
        soma = sum(elementos)
        expressao = " + ".join([f"{x}" for x in elementos])
        return soma, f"\\sum_{{i={i}}}^{{n={n}}} {variavel}_{{i}} = {expressao} = {soma}"

    elif tipo_operacao == "Soma dos Quadrados (X ou Y)":
        elementos = dados[i-1:n]  # Pegando os elementos entre os limites i e n
        soma_quadrados = sum(x**2 for x in elementos)
        expressao = " + ".join([f"{x}^2" for x in elementos])
        return soma_quadrados, f"\\sum_{{i={i}}}^{{n={n}}} {variavel}_{{i}}^2 = {expressao} = {soma_quadrados}"

    elif tipo_operacao == "Quadrado da Soma (X ou Y)":
        elementos = dados[i-1:n]  # Pegando os elementos entre os limites i e n
        soma = sum(elementos)
        expressao = " + ".join([f"{x}" for x in elementos])
        return soma**2, f"\\left(\\sum_{{i={i}}}^{{n={n}}} {variavel}_{{i}} \\right)^2 = \\left({expressao}\\right)^2 = {soma**2}"
    
    elif tipo_operacao == "Soma de Produtos (X e Y)":
        elementos_X = dados_X[i-1:n]
        elementos_Y = dados_Y[i-1:n]
        soma_produtos = sum(x * y for x, y in zip(elementos_X, elementos_Y))
        expressao = " + ".join([f"{x} \\cdot {y}" for x, y in zip(elementos_X, elementos_Y)])
        return soma_produtos, f"\\sum_{{i={i}}}^{{n={n}}} (X_{{i}} \\cdot Y_{{i}}) = {expressao} = {soma_produtos}"
    
    elif tipo_operacao == "Produto da Soma (X e Y)":
        elementos_X = dados_X[i-1:n]
        elementos_Y = dados_Y[i-1:n]
        soma_X = sum(elementos_X)
        soma_Y = sum(elementos_Y)
        expressao_X = " + ".join([f"{x}" for x in elementos_X])
        expressao_Y = " + ".join([f"{y}" for y in elementos_Y])
        return soma_X * soma_Y, f"\\left(\\sum_{{i={i}}}^{{n={n}}} X_{{i}} \\right) \\cdot \\left(\\sum_{{i={i}}}^{{n={n}}} Y_{{i}} \\right) = \\left({expressao_X}\\right) \\cdot \\left({expressao_Y}\\right) = {soma_X * soma_Y}"
    
    elif tipo_operacao == "Produto da Soma de Quadrados (X e Y)":
        elementos_X = dados_X[i-1:n]
        elementos_Y = dados_Y[i-1:n]
        soma_quadrados_X = sum(x**2 for x in elementos_X)
        soma_quadrados_Y = sum(y**2 for y in elementos_Y)
        expressao_X = " + ".join([f"{x}^2" for x in elementos_X])
        expressao_Y = " + ".join([f"{y}^2" for y in elementos_Y])
        return soma_quadrados_X * soma_quadrados_Y, f"\\left(\\sum_{{i={i}}}^{{n={n}}} X_{{i}}^2 \\right) \\cdot \\left(\\sum_{{i={i}}}^{{n={n}}} Y_{{i}}^2 \\right) = \\left({expressao_X}\\right) \\cdot \\left({expressao_Y}\\right) = {soma_quadrados_X * soma_quadrados_Y}"
    
    elif tipo_operacao == "Soma de Quadrados de Produtos (X e Y)":
        elementos_X = dados_X[i-1:n]
        elementos_Y = dados_Y[i-1:n]
        soma_quadrados_produtos = sum((x**2) * (y**2) for x, y in zip(elementos_X, elementos_Y))
        expressao = " + ".join([f"({x}^2 \\cdot {y}^2)" for x, y in zip(elementos_X, elementos_Y)])
        return soma_quadrados_produtos, f"\\sum_{{i={i}}}^{{n={n}}} (X_{{i}}^2 \\cdot Y_{{i}}^2) = {expressao} = {soma_quadrados_produtos}"

# Determinar os dados que serão utilizados (X ou Y) com base na escolha do usuário
dados = dados_X if variavel == "X" else dados_Y

# Processar o somatório e exibir o resultado
if st.button("Calcular Somatório"):
    resultado, expressao = somatorio(operacao, dados, dados_X, dados_Y, i, n)
    
    if resultado is not None and expressao is not None:
        # Exibir a expressão do somatório usando símbolos matemáticos
        st.latex(expressao)
        
        # Exibir o resultado do somatório
        st.write(f"**Resultado do somatório**: {resultado}")


















# import streamlit as st

# # Título do aplicativo
# st.title("Somatório de forma prática")

# # Entrada para os dados (X)
# st.write("Insira os valores da variável X, separados por vírgulas:")
# dados_input_X = st.text_area("Exemplo para X: 1, 2, 3, 4, 5", value="1, 2, 3, 4, 5")

# # Entrada para os dados (Y)
# st.write("Insira os valores da variável Y, separados por vírgulas (mesmo tamanho que X):")
# dados_input_Y = st.text_area("Exemplo para Y: 5, 4, 3, 2, 1", value="5, 4, 3, 2, 1")

# # Entrada para o limite inferior (LI)
# i = st.number_input("Informe o limite inferior (i ou LI):", min_value=1, value=1)

# # Converter os dados de entrada em uma lista de floats
# try:
#     dados_X = list(map(float, dados_input_X.split(',')))
#     dados_Y = list(map(float, dados_input_Y.split(',')))
# except ValueError:
#     st.error("Por favor, insira os valores corretamente separados por vírgulas.")

# # Verificar se o tamanho das listas de X e Y é o mesmo
# if len(dados_X) != len(dados_Y):
#     st.error("As listas de X e Y precisam ter o mesmo tamanho.")

# # Entrada para o limite superior (LS) iniciando com o tamanho de X
# n = st.number_input("Informe o limite superior (n ou LS):", min_value=i, value=len(dados_X))

# # Seletor para escolher se as operações serão feitas em X ou Y
# variavel = st.selectbox("Selecione a variável para aplicar as operações:", ("X", "Y"))

# # Opções para o tipo de operação
# operacao = st.selectbox(
#     "Selecione o tipo de operação:",
#     ("Soma Simples (X ou Y)", "Soma dos Quadrados (X ou Y)", "Quadrado da Soma (X ou Y)", 
#      "Soma de Produtos (X e Y)", "Produto da Soma (X e Y)", "Produto da Soma de Quadrados (X e Y)")
# )

# # Definir a função para o somatório
# def somatorio(tipo_operacao, dados, dados_X, dados_Y, i, n):
#     if n > len(dados_X) or n > len(dados_Y):
#         st.error("O limite superior não pode ser maior que o tamanho da lista de dados.")
#         return None, None

#     if tipo_operacao == "Soma Simples (X ou Y)":
#         elementos = dados[i-1:n]  # Pegando os elementos entre os limites i e n
#         soma = sum(elementos)
#         expressao = " + ".join([f"{x}" for x in elementos])
#         return soma, f"\\sum_{{i={i}}}^{{n={n}}} {variavel}_{{i}} = {expressao} = {soma}"

#     elif tipo_operacao == "Soma dos Quadrados (X ou Y)":
#         elementos = dados[i-1:n]  # Pegando os elementos entre os limites i e n
#         soma_quadrados = sum(x**2 for x in elementos)
#         expressao = " + ".join([f"{x}^2" for x in elementos])
#         return soma_quadrados, f"\\sum_{{i={i}}}^{{n={n}}} {variavel}_{{i}}^2 = {expressao} = {soma_quadrados}"

#     elif tipo_operacao == "Quadrado da Soma (X ou Y)":
#         elementos = dados[i-1:n]  # Pegando os elementos entre os limites i e n
#         soma = sum(elementos)
#         expressao = " + ".join([f"{x}" for x in elementos])
#         return soma**2, f"\\left(\\sum_{{i={i}}}^{{n={n}}} {variavel}_{{i}} \\right)^2 = \\left({expressao}\\right)^2 = {soma**2}"
    
#     elif tipo_operacao == "Soma de Produtos (X e Y)":
#         elementos_X = dados_X[i-1:n]
#         elementos_Y = dados_Y[i-1:n]
#         soma_produtos = sum(x * y for x, y in zip(elementos_X, elementos_Y))
#         expressao = " + ".join([f"{x} \\cdot {y}" for x, y in zip(elementos_X, elementos_Y)])
#         return soma_produtos, f"\\sum_{{i={i}}}^{{n={n}}} (X_{{i}} \\cdot Y_{{i}}) = {expressao} = {soma_produtos}"
    
#     elif tipo_operacao == "Produto da Soma (X e Y)":
#         elementos_X = dados_X[i-1:n]
#         elementos_Y = dados_Y[i-1:n]
#         soma_X = sum(elementos_X)
#         soma_Y = sum(elementos_Y)
#         expressao_X = " + ".join([f"{x}" for x in elementos_X])
#         expressao_Y = " + ".join([f"{y}" for y in elementos_Y])
#         return soma_X * soma_Y, f"\\left(\\sum_{{i={i}}}^{{n={n}}} X_{{i}} \\right) \\cdot \\left(\\sum_{{i={i}}}^{{n={n}}} Y_{{i}} \\right) = \\left({expressao_X}\\right) \\cdot \\left({expressao_Y}\\right) = {soma_X * soma_Y}"
    
#     elif tipo_operacao == "Produto da Soma de Quadrados (X e Y)":
#         elementos_X = dados_X[i-1:n]
#         elementos_Y = dados_Y[i-1:n]
#         soma_quadrados_X = sum(x**2 for x in elementos_X)
#         soma_quadrados_Y = sum(y**2 for y in elementos_Y)
#         expressao_X = " + ".join([f"{x}^2" for x in elementos_X])
#         expressao_Y = " + ".join([f"{y}^2" for y in elementos_Y])
#         return soma_quadrados_X * soma_quadrados_Y, f"\\left(\\sum_{{i={i}}}^{{n={n}}} X_{{i}}^2 \\right) \\cdot \\left(\\sum_{{i={i}}}^{{n={n}}} Y_{{i}}^2 \\right) = \\left({expressao_X}\\right) \\cdot \\left({expressao_Y}\\right) = {soma_quadrados_X * soma_quadrados_Y}"

# # Determinar os dados que serão utilizados (X ou Y) com base na escolha do usuário
# dados = dados_X if variavel == "X" else dados_Y

# # Processar o somatório e exibir o resultado
# if st.button("Calcular Somatório"):
#     resultado, expressao = somatorio(operacao, dados, dados_X, dados_Y, i, n)
    
#     if resultado is not None and expressao is not None:
#         # Exibir a expressão do somatório usando símbolos matemáticos
#         st.latex(expressao)
        
#         # Exibir o resultado do somatório
#         st.write(f"**Resultado do somatório**: {resultado}")











# import streamlit as st

# # Título do aplicativo
# st.title("Somatório de forma prática")

# # Entrada para os dados (X)
# st.write("Insira os valores da variável X, separados por vírgulas:")
# dados_input_X = st.text_area("Exemplo para X: 1, 2, 3, 4, 5", value="1, 2, 3, 4, 5")

# # Entrada para os dados (Y)
# st.write("Insira os valores da variável Y, separados por vírgulas (mesmo tamanho que X):")
# dados_input_Y = st.text_area("Exemplo para Y: 5, 4, 3, 2, 1", value="5, 4, 3, 2, 1")

# # Entrada para o limite inferior (LI)
# i = st.number_input("Informe o limite inferior (i ou LI):", min_value=1, value=1)

# # Converter os dados de entrada em uma lista de floats
# try:
#     dados_X = list(map(float, dados_input_X.split(',')))
#     dados_Y = list(map(float, dados_input_Y.split(',')))
# except ValueError:
#     st.error("Por favor, insira os valores corretamente separados por vírgulas.")

# # Verificar se o tamanho das listas de X e Y é o mesmo
# if len(dados_X) != len(dados_Y):
#     st.error("As listas de X e Y precisam ter o mesmo tamanho.")

# # Entrada para o limite superior (LS) iniciando com o tamanho de X
# n = st.number_input("Informe o limite superior (n ou LS):", min_value=i, value=len(dados_X))

# # Opções para o tipo de operação
# operacao = st.selectbox(
#     "Selecione o tipo de operação:",
#     ("Soma Simples", "Soma dos Quadrados", "Quadrado da Soma", "Soma de Produtos", "Produto da Soma", "Produto da Soma de Quadrados")
# )

# # Definir a função para o somatório
# def somatorio(tipo_operacao, dados_X, dados_Y, i, n):
#     if n > len(dados_X) or n > len(dados_Y):
#         st.error("O limite superior não pode ser maior que o tamanho da lista de dados.")
#         return None, None

#     if tipo_operacao == "Soma Simples":
#         elementos = dados_X[i-1:n]  # Pegando os elementos entre os limites i e n
#         soma = sum(elementos)
#         expressao = " + ".join([f"{x}" for x in elementos])
#         return soma, f"\\sum_{{i={i}}}^{{n={n}}} X_{{i}} = {expressao} = {soma}"

#     elif tipo_operacao == "Soma dos Quadrados":
#         elementos = dados_X[i-1:n]  # Pegando os elementos entre os limites i e n
#         soma_quadrados = sum(x**2 for x in elementos)
#         expressao = " + ".join([f"{x}^2" for x in elementos])
#         return soma_quadrados, f"\\sum_{{i={i}}}^{{n={n}}} X^2_{{i}} = {expressao} = {soma_quadrados}"

#     elif tipo_operacao == "Quadrado da Soma":
#         elementos = dados_X[i-1:n]  # Pegando os elementos entre os limites i e n
#         soma = sum(elementos)
#         expressao = " + ".join([f"{x}" for x in elementos])
#         return soma**2, f"\\left(\\sum_{{i={i}}}^{{n={n}}} X_{{i}} \\right)^2 = \\left({expressao}\\right)^2 = {soma**2}"
    
#     elif tipo_operacao == "Soma de Produtos":
#         elementos_X = dados_X[i-1:n]
#         elementos_Y = dados_Y[i-1:n]
#         soma_produtos = sum(x * y for x, y in zip(elementos_X, elementos_Y))
#         expressao = " + ".join([f"{x} * {y}" for x, y in zip(elementos_X, elementos_Y)])
#         return soma_produtos, f"\\sum_{{i={i}}}^{{n={n}}} (X_{{i}} \\cdot Y_{{i}}) = {expressao} = {soma_produtos}"
    
#     elif tipo_operacao == "Produto da Soma":
#         elementos_X = dados_X[i-1:n]
#         elementos_Y = dados_Y[i-1:n]
#         soma_X = sum(elementos_X)
#         soma_Y = sum(elementos_Y)
#         expressao_X = " + ".join([f"{x}" for x in elementos_X])
#         expressao_Y = " + ".join([f"{y}" for y in elementos_Y])
#         return soma_X * soma_Y, f"\\left(\\sum_{{i={i}}}^{{n={n}}} X_{{i}} \\right) \\cdot \\left(\\sum_{{i={i}}}^{{n={n}}} Y_{{i}} \\right) = \\left({expressao_X}\\right) \\cdot \\left({expressao_Y}\\right) = {soma_X * soma_Y}"
    
#     elif tipo_operacao == "Produto da Soma de Quadrados":
#         elementos_X = dados_X[i-1:n]
#         elementos_Y = dados_Y[i-1:n]
#         soma_quadrados_X = sum(x**2 for x in elementos_X)
#         soma_quadrados_Y = sum(y**2 for y in elementos_Y)
#         expressao_X = " + ".join([f"{x}^2" for x in elementos_X])
#         expressao_Y = " + ".join([f"{y}^2" for y in elementos_Y])
#         return soma_quadrados_X * soma_quadrados_Y, f"\\left(\\sum_{{i={i}}}^{{n={n}}} X_{{i}}^2 \\right) \\cdot \\left(\\sum_{{i={i}}}^{{n={n}}} Y_{{i}}^2 \\right) = \\left({expressao_X}\\right) \\cdot \\left({expressao_Y}\\right) = {soma_quadrados_X * soma_quadrados_Y}"


# # Processar o somatório e exibir o resultado
# if st.button("Calcular Somatório"):
#     resultado, expressao = somatorio(operacao, dados_X, dados_Y, i, n)
    
#     if resultado is not None and expressao is not None:
#         # Exibir a expressão do somatório usando símbolos matemáticos
#         st.latex(expressao)
        
#         # Exibir o resultado do somatório
#         st.write(f"**Resultado do somatório**: {resultado}")
