'''
dia = int(input('digite o dia'))
mes = int(input('digite o mes'))
ano = int(input('digite o ano'))

if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and ano <= 2025:
    print('data valida')
else:
    print('data invalida')
'''
data = input('digite a data de hoje no formato dd/mm/aaaa  ')

dia = data.split('/')[0]
mes = data.split('/')[1]
ano = data.split('/')[2]
dia = int(dia)
mes = int(mes)
ano = int(ano)

if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and ano <= 2025:
    print('data valida')
else:
    print('data invalida')







