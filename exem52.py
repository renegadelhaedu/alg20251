alunos = []

op = 99

while op != 0:
    print('----MENU----')
    print('1-cadastrar usuario')
    print('2-remover usuario')
    print('3-listar alunos')

    op = int(input('digite a opcao desejada '))

    if op == 1:
        nome = input('digite seu nome')
        mat = input('digite a matricula')
        curso = input('digite seu curso')
        mens = float(input('digite o valor da mensalidade'))

        alunos.append([nome, mat, curso, mens])
        print('aluno cadastrado com sucesso \n')
    elif op == 2:
        mat_remov = input('digite a matricula do aluno para remover ')
        indice = -1
        for i in range(len(alunos)):
            if mat_remov == alunos[i][1]:
                indice = i
        if indice != -1:
            alunos.pop(indice)
            print('aluno removido com sucesso')
        else:
            print('matricula nao encontrada')
    elif op == 3:
        for aluno in alunos:
            print(aluno)