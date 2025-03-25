#faça um algoritmo que receba um valor inicial do usuário e
#exiba o valor final apos alguns anos. o usuario deve informar
#o ano inicial,o ano final e cada ano deve ser informado o valor da selic

valor = float(input('digite o valor do investimento'))
ano_inicial = int(input('digite o ano do investimento inicial'))
ano_final = int(input('digite o ano da retirada do valor'))

for ano in range(ano_inicial, ano_final + 1):
    print('Estamos em ', ano, end=' - ')
    selic = float(input('qual o valor da selic deste ano '))

    if selic <= 8.5:
        juros = selic * 0.7
        valor = valor * (1 + juros/100)
    else:
        valor = valor * (1 + 0.06)

valor = round(valor, 2)
anos = ano_final - ano_inicial
print(f'apos {anos} anos o valor final foi {valor}')




