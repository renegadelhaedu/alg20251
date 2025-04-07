compra = float(input('digite o valor da compra'))
print('valor da compra - juros - qtde parcelas - valor parcela')
print(f'{compra}      - {0}     - {1}     - {compra}')
juros = 10
for parcela in range(3, 13, 3):
    total = compra * (1 + juros / 100)
    valor_parcela = total / parcela
    print(f'{total}      - {juros}     - {parcela}     - {valor_parcela}')

    juros += 5
