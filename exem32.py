#o nepa está precisando de um sistema que entreviste
#50 alunos fazendo perguntas objetivas sim ou nao.
#modele o sistema para listar apenas os alunos que possuam
#mais aderencia ao projeto

for i in range(50):
    nome = input('digite seu nome')
    q1 = input('digite sim ou nao se vc tem disponibilidade de aprender coisas novas')
    q2 = input('digite sim ou nao se vc tem sabe interagir em grupo')
    q3 = input('digite sim ou nao se vc pode ajudar os colegas')
    q4 = input('digite sim ou nao se vc gosta de tecnologia')
    contagem = 0
    if q1.lower() == 'sim':
        contagem += 1
    if q2.lower() == 'sim':
        contagem += 1
    if q3.lower() == 'sim':
        contagem += 1
    if q4.lower() == 'sim':
        contagem += 1

    if contagem >= 3:
        print(nome, ' voce foi selecionado para o projeto')
    else:
        print(nome, ' voce nao foi selecionado para o projeto')

