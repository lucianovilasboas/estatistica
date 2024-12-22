import streamlit as st
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulação do Problema de Monty Hall", page_icon="🚪", layout='wide')

# Definindo a simulação do problema de Monty Hall
def monty_hall_simulation(num_trials, switch):
    win_count = 0
    for _ in range(num_trials):
        # Colocando o carro aleatoriamente em uma das três portas
        car_door = random.randint(0, 2)

        # O jogador escolhe uma porta aleatoriamente
        player_choice = random.randint(0, 2)

        # Apresentador abre uma das portas que não tem o carro e não é a escolha do jogador
        available_doors = [i for i in range(3) if i != player_choice and i != car_door]
        monty_door = random.choice(available_doors)

        # Se o jogador decidir trocar, atualiza a escolha dele para a outra porta que restou
        if switch:
            player_choice = [i for i in range(3) if i != player_choice and i != monty_door][0]

        # Conta vitória se o jogador escolher a porta com o carro
        if player_choice == car_door:
            win_count += 1

    return win_count

# Interface do Streamlit
st.title('🚪 Simulação do Problema de Monty Hall')
st.write('Este aplicativo simula o famoso problema de Monty Hall, onde um jogador tem que escolher entre três portas para encontrar um carro.')
st.image("https://github.com/lucianovilasboas/medium-monty-hall/blob/main/Monty_hall_problem.jpg?raw=true", caption="Problema de Monty Hall", use_column_width=False)
st.write("---")


# Entrada do número de simulações
num_trials = st.number_input('Escolha o número de simulações', min_value=1, value=1000)

# Escolha de trocar ou não de porta
switch = st.selectbox('Você deseja trocar de porta?', ('Sim', 'Não'))
switch = True if switch == 'Sim' else False

# Botão para rodar a simulação
if st.button('Executar Simulação'):
    win_count = monty_hall_simulation(num_trials, switch)
    win_percentage = (win_count / num_trials) * 100

    # Resultados
    st.write(f'O número de vitórias foi: {win_count}')
    st.write(f'A porcentagem de vitórias foi: {win_percentage:.2f}%')

    if switch:
        st.write('Trocar de porta geralmente aumenta suas chances de vencer para cerca de 66,67%.')
    else:
        st.write('Ficar com a mesma porta geralmente dá a você uma chance de 33,33% de vencer.')

    # Gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(['Vitórias', 'Derrotas'], [win_count, num_trials - win_count], color=['green', 'red'])
    ax.set_ylabel('Número de Ocorrências')
    ax.set_title('Resultados da Simulação do Problema de Monty Hall')

    st.pyplot(fig)
else:
    st.info('Aguardando simulação')
