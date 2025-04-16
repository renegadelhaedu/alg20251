alunos = []

op = 99

while op != 0:
    print('----MENU----')
    print('1-cadastrar usuario')
    print('2-remover usuario')
    print('3-listar alunos')
    print('4-buscar nome')

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
    elif op == 4:
        nome_busca = input('digite o nome para busca ')
        for aluno in alunos:
            if nome_busca == aluno[0]:
                print(f'Nome: {aluno[0]}')
                print(f'Matricula: {aluno[1]}')
                print(f'Curso: {aluno[2]}')
                print(f'mensalidade: {aluno[3]}')
            print(' - ')

    elif op == 5:
        soma = 0
        qtde = 0
        curso = input('digite o curso para descobrir a media ')

        for aluno in alunos:
            if curso == aluno[2]:
                soma += aluno[3]
                qtde += 1

        media = soma / qtde
        print(f'a media de mensalidades do curso {curso} foi {media}')
