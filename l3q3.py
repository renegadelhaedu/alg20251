#questao 3

nome = input('digite seu nome')
while(len(nome) <= 3):
    nome = input('digite seu nome')

idade = int(input('digite sua idade'))
while idade < 0 or  idade > 150:
    idade = int(input('digite sua idade'))

salario = float(input('qual seu salario'))
while salario <= 0:
    salario = float(input('qual seu salario'))

est = input('digite seu estado civil')
while est != 's' or est != 'c' or est != 'd' or est != 'v':
    est = input('digite seu estado civil')

