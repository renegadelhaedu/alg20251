# leia do usuário o nome, a idade e o salário dele: aumente o salário
# proporcionando 5% a cada 10 anos de vida. caso ele tenha mais de 50 anos,
# aumente 15% a mais.

nome = input('digite seu nome')
idade = int(input('digite sua idade'))
salario = float(input('digite seu salario'))

perc_aumento = (idade // 10) * 5
salario_final = salario * (1 + (perc_aumento / 100))
#salario *= (1 + (perc_aumento / 100))

if idade > 50:
    salario_final = salario_final * 1.15

print('o salario final deste colaborador será', salario_final)