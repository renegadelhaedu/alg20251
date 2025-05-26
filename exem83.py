atletas = []

op = 9
while op != 0:
    print('____MENU-_____')
    print('1-inserir atleta')
    print('2-remover atleta')
    print('3-salvar lista atletas em arquivo')

    op = int(input('digite a opcao desejada'))

    if op == 1:
        nome = input('digite seu nome')
        atletas.append(nome)
    elif op == 2:
        nome = input('digite o nome para remover')
        if nome in atletas:
            atletas.remove(nome)
    elif op == 3:
        file = open('meusatletas.txt','w')
        file.write('Esses são nossos atletas queridos:\n')
        for nome in atletas:
            file.write(nome + '\n')
        file.close()













