nome = ''
qtde = 0

while(nome != 'sair'):

    nome = input('digite seu nome')
    if nome == 'rene':
        continue
    elif nome == 'sair':
        break
    qtde += 1

print(qtde)