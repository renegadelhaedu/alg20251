'''
sfadfasdf
sadfasdfsadfsadfqwerqwerqwe
'''

salario = float(input('digite seu salario: '))

if salario > 0 and salario <= 280:
    aumento = salario * 0.2
    perc = 20
elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
    perc = 15
elif salario > 700 and salario <= 1500:
    aumento = round(salario * 0.1, 2)
    perc = 10
elif salario > 1500:
    aumento = round(salario * 0.05, 2)
    perc = 5
else:
    print('nao aceito numero negativo')
    aumento = 0


#estou fazendo esse para exibir os valores apenas para casos com
#salario positivo
if aumento > 0:
    print('seu salario era ', salario)
    print('voce recebeu um aumento percentual de ', perc)
    print('isso corresponde a aumento em reais de ', aumento)
    final = salario + aumento
    final = round(final, 2)
    print('seu salario final é ', final)






