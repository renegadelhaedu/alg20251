#estrutura de dados: dicionário/mapa
#par: chave e valor
#chaves são únicas
#nao ha índice, nem ordem


#declara um dicionario vazio
pessoas = dict()

#adicionar dentro do dicionario
pessoas['1230913124'] = 'rene'

#declarar um dicionario com valores
papas = {'francisco':'88 anos', 'joao paulo':83, 'bento16':89,1.3:4}

#percorrer um dicionario
for papa in papas.values():
    print(papa)
print('\n-------------------------\n')
for papa in papas:
    print(papas[papa])

nome_papa = input('digite o nome do papa que vc quer buscar: ')

print('\n\n\n\n\n')

if nome_papa in papas:
    print(papas.get(nome_papa)) #metodo get recebe a chave e retorna o valor associado
    print(papas[nome_papa]) #entre colchetes, dê a chave e retorna o valor associado
else:
    print('esse papa nao existe')

