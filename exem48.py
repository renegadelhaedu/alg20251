pessoas = ['casa','vida','casa']

#contar quantas vezes aquele item aparece na lista
print(pessoas.count('casa'))

qtde = 0
busca = input('digite o nome que vc procura')
for item in pessoas:
    if item == busca:
        qtde += 1

