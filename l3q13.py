#questao 13

base = int(input('digte um numero referente a base'))
exp = int(input('digte um numero referente a um expoente'))

resposta = 1

for i in range(exp):
    resposta *= base

print(resposta)