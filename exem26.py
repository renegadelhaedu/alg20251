#desenvolva um algoritmo que ajude o professor a ler o nome e nota da prova
#dos 55 alunos do p1. o algoritmo deve verificar a menor, a maior e
# a média das notas. Ele também deve aumentar 1 ponto para os alunos que
#ficaram com nota abaixo de 5.

maior = 0
menor = 10
soma = 0
for i in range(55):
    nome = input('digite seu nome')
    nota = float(input('digite sua nota'))

    if nota < menor:
        menor = nota

    if nota > maior:
        maior = nota

    if nota < 5:
        nota += 1

    soma = soma + nota


media = soma / (i+1)

print('a maior nota foi ', maior)








