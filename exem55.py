nomes = ['rene','maria']

nomes.insert(1,'rafa')
nome_busca = 'rene'
if nomes.count(nome_busca) > 0:
    nomes.remove(nome_busca)
else:
    print('pessoa inexistente na lista')

print(nomes)