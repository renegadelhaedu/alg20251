#pip install matplotlib

import matplotlib.pyplot as plt

peso = [100, 70, 93, 65, 69]
altura = [179, 170, 175, 172, 170]
nomes = ['keven','lucas','rafael','jonathas','rene']

#cria o grafico contendo o valor das duas listas
plt.scatter(peso,altura)
#exibe o gráfico na tela
plt.show()

