#crie uma lista
pessoas = []
#adicione 3 nomes dentro da lista
pessoas.append('mirela')
pessoas.append('raissa')
pessoas.append('tomaz')
#percorra a lista verificando se o nome inicia com a letra m, se sim, exiba
for nome in pessoas:
    if nome[0] == 'm':
        print(nome)

