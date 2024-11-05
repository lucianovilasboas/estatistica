import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Gerador de Histograma", page_icon="📉",layout="wide")
# Título do aplicativo
st.markdown("<h1 style='text-align: center;'>📉 Gerador de Histograma</h1>", unsafe_allow_html=True)
st.write("Este aplicativo gera um histograma a partir dos dados inseridos, permitindo ajustar o número de bins e o tamanho de cada bin.")
st.write("---")

# Entrada dos dados
st.sidebar.write("# Entre com os dados")
st.sidebar.write("Insira os dados separados por vírgulas:")
dados_input = st.sidebar.text_area("Exemplo: 6.67, 6.82, 6.90, 7.05, 7.10")

# Converter a string de entrada em uma lista de floats
if dados_input:
    try:
        dados = list(map(float, dados_input.split(','))) 
        
        # Identificar os valores mínimo e máximo dos dados
        min_val, max_val = min(dados), max(dados)

        # Escolha o número de bins
        # bins = st.sidebar.slider('Escolha o número de bins (faixas)', min_value=1, max_value=20, value=5)

        bins = st.sidebar.slider(
            'Escolha o número de bins (faixas)',
            min_value=1,
            max_value=20,
            value=5,
            format="%d"  # Exibe os valores como números inteiros
)
        
        # # Permitir o ajuste do tamanho de cada bin
        # bin_size = st.sidebar.slider('Escolha o tamanho do bin', min_value=0.01, max_value=(max_val - min_val) / 2, value=(max_val - min_val) / bins)

        # Gerar os limites das faixas (bins) corretamente usando np.linspace para garantir a quantidade exata de bins
        bin_edges = np.linspace(min_val, max_val, bins + 1)


        # Gerar o histograma e calcular a frequência de cada bin
        hist, bin_edges = np.histogram(dados, bins=bin_edges)

        fig, ax = plt.subplots()
        n, bins, patches = ax.hist(dados, bins=bin_edges, edgecolor='black')
        
        # Adicionar os valores das frequências no topo de cada barra
        for i in range(len(patches)):
            ax.text(patches[i].get_x() + patches[i].get_width() / 2, patches[i].get_height(),
                    str(int(patches[i].get_height())), ha='center', va='bottom')
        
        # Configurações de rótulos e título
        ax.set_xlabel('Faixas de Valores')
        ax.set_ylabel('Frequência')
       
        # Exibir o gráfico
        st.pyplot(fig)

        # Exibir os intervalos e frequências
        st.write("### Intervalos e Frequências:")
        for i in range(len(hist)):
            st.write(f"Intervalo {i + 1}: [{bin_edges[i]:.2f}, {bin_edges[i+1]:.2f}] - Frequência: {hist[i]}")
    
    except ValueError:
        st.error("Por favor, insira os dados corretamente no formato numérico, separados por vírgula.")
else:
    st.info("Aguardando a entrada dos dados.")












# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt

# # Título do aplicativo
# st.title("Gerador de Histograma com Ajuste de Bins e Tamanho dos Bins")

# # Entrada dos dados
# st.write("Insira os dados separados por vírgulas:")
# dados_input = st.text_area("Exemplo: 6.67, 6.82, 6.90, 7.05, 7.10")

# # Converter a string de entrada em uma lista de floats
# if dados_input:
#     try:
#         dados = list(map(float, dados_input.split(',')))
        
#         # Identificar os valores mínimo e máximo dos dados
#         min_val, max_val = min(dados), max(dados)

#         # Escolha o número de bins
#         bins = st.slider('Escolha o número de bins (faixas)', min_value=1, max_value=20, value=5)

#         # Permitir o ajuste do tamanho de cada bin
#         bin_size = st.slider('Escolha o tamanho do bin', min_value=0.01, max_value=(max_val - min_val) / 2, value=(max_val - min_val) / bins)

#         # Gerar os limites das faixas (bins) com base no tamanho do bin escolhido
#         bin_edges = np.arange(min_val, max_val + bin_size, bin_size)

#         # Gerar o histograma
#         fig, ax = plt.subplots()
#         ax.hist(dados, bins=bin_edges, edgecolor='black')

#         # Configurações de rótulos e título
#         ax.set_xlabel('Faixas de Valores')
#         ax.set_ylabel('Frequência')
#         ax.set_title('Histograma com ajuste de bins e tamanho dos bins')

#         # Exibir o gráfico
#         st.pyplot(fig)
#     except ValueError:
#         st.error("Por favor, insira os dados corretamente no formato numérico, separados por vírgula.")
# else:
#     st.info("Aguardando a entrada dos dados.")















# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt

# # Título do aplicativo
# st.title("Gerador de Histograma com Ajuste de Bins")

# # Entrada dos dados
# st.write("Insira os dados separados por vírgulas:")
# dados_input = st.text_area("Exemplo: 6.67, 6.82, 6.90, 7.05, 7.10")

# # Converter a string de entrada em uma lista de floats
# if dados_input:
#     try:
#         dados = list(map(float, dados_input.split(',')))
        
#         # Escolha o número de bins
#         bins = st.slider('Escolha o número de bins (faixas)', min_value=1, max_value=20, value=5)
        
#         # Gerar o histograma
#         fig, ax = plt.subplots()
#         ax.hist(dados, bins=bins, edgecolor='black')
        
#         # Configurações de rótulos e título
#         ax.set_xlabel('Faixas de Valores')
#         ax.set_ylabel('Frequência')
#         ax.set_title('Histograma com ajuste de bins')

#         # Exibir o gráfico
#         st.pyplot(fig)
#     except ValueError:
#         st.error("Por favor, insira os dados corretamente no formato numérico, separados por vírgula.")
# else:
#     st.info("Aguardando a entrada dos dados.")
