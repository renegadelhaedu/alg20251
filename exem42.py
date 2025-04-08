#crie uma lista vazia e leia o nome de todos os alunos da sala,
# colocando cada nome dentro da lista. continue lendo que seja
#digitado a palavra fim.

nomes = []

while True:
    nome = input('digite seu nome')
    if nome == 'fim':
        break
    #acrescentar no final da lista
    nomes.append(nome)

#no final informe quantas pessoas estao em sala
print(len(nomes))