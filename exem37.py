'''
desenvolva um algoritmo que leia o nome de todos os alunos
que estiveram em sala hoje. o algoritmo deve parar a leitura
quando for digitado a palavra "fim". no final, diga quantos
alunos estiveram em sala
'''

contador = 0
nome = ''

while nome != 'fim':
    nome = input('qual o nome do aluno(a)?')
    contador += 1

print('quantidade de alunos em sala', contador - 1)






