people = dict()

for i in range(3):
    cpf = input('digite seu cpf ')
    nome = input('digite seu nome ')
    qtde = int(input('digite a qtde de pessoas que vc dancou '))

    people[cpf] = [nome, qtde]
    print('Pessoas adicionada com sucesso')

soma = 0
for cpf in people:
    soma = soma + people[cpf][1]

soma += len(people)
print(f'no total {soma} dancaram nesta noite')