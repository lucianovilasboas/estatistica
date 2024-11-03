import streamlit as st

# Configurações iniciais da página
st.set_page_config(page_title="Apps de Estatística", page_icon="📊")

# Título da página
st.title("📊 Apps de Estatística")
st.write("Bem-vindo à página de aplicativos de apoio para a disciplina de Estatística e Probabilidade!")

# Informações sobre o curso
st.header("Sobre o Curso")
st.write("""
Este projeto foi desenvolvido para apoiar o ensino da disciplina de Estatística e Probabilidade 
do curso de Tecnologia em Processos Gerenciais do IFMG - Campus Ponte Nova. 
A disciplina explora os conceitos fundamentais de estatística, 
como análise de dados, probabilidades, intervalos de confiança, testes de hipóteses, e muito mais. 
Os aplicativos disponíveis nesta página foram criados com o intuito de facilitar a compreensão prática desses conceitos.
""")

# Informações sobre o professor
st.header("Sobre o Professor Luciano")
st.write("""
O professor Luciano Vilas Boas é o responsável pela disciplina e desenvolveu esses aplicativos como uma ferramenta de apoio 
para tornar a aprendizagem mais interativa e acessível. 

Professor Luciano possui Graduação e Mestrado em Ciência da Computação pela UFOP com experiência em Ciência da Computação e Docência, tendo atuado em diversas áreas, 
como Programação, Desenvolvimento Web, Recuperação da Informação, Aprendizado de Máquina e Ciência de Dados. 
Atualmente, é Docente e Diretor Geral no IFMG Campus Ponte Nova.
""")
st.write("🔗 [Acesse o perfil do Professor Luciano no Streamlit](https://share.streamlit.io/user/lucianovilasboas)")

# Informações de contato
st.header("Contato")
st.write("""
Para dúvidas ou mais informações, entre em contato pelo e-mail:
📧 luciano.espiridiao@ifmg.edu.br
""")

# Lista de Aplicativos de Apoio
st.header("Aplicativos de Apoio em Estatística")
st.write("Explore os aplicativos disponíveis para aprofundar seu entendimento em Estatística e Probabilidade:")

# Exemplos de links de aplicativos
st.write("- [Simulador de Lançamento de Dados e Moedas](Lancamento)")
st.write("- [Sumarização de dados](Sumarizacao)")
st.write("- [Calculadora de Média e Desvio Padrão](Desvio_Padrao)")
st.write("- [Distribuições de Probabilidade](Gerador)")
st.write("- [Canculador de Somatórios 1](Sumatoruium)")
st.write("- [Canculador de Somatórios 2](Sumatoruium_xy)")

# Rodapé
st.write("---")
st.write("© 2024 IFMG Campus Ponte Nova - Disciplina de Estatística e Probabilidade - Professor Luciano")
