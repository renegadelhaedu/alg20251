#pip install matplotlib

import matplotlib.pyplot as plt

idades = [36,21,25,23,17,16,47]
nomes = ['rene','asa','caca','popo','xuxu','pele','toinho']

#cria o grafico contendo o valor das duas listas
plt.bar( nomes, idades)
#exibe o gráfico na tela
plt.show()

