import numpy as np

# Gere uma sequencia de alturas com n=21 em uma lista chamada alturas. Em seguida, crie um DataFrame chamado df com uma coluna chamada 'Altura' e os valores da lista alturas. Por fim, crie um histograma com os valores de df['Altura'].
alturas = [1.70, 1.71, 1.72, 1.73, 1.74, 1.75, 1.76, 1.77, 1.78, 1.79, 1.80, 1.81, 1.82, 1.83, 1.84, 1.85, 1.86, 1.87, 1.88, 1.89, 1.90]


# gere outra lista com pesos de 60 a 80 kg com 21 elementos e distribuição normal
pesos = np.random.normal(70, 5, 21)
print(pesos)



