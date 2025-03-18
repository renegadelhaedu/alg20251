litros = float(input('digite a quantidade de litros'))
tipo = input('digite o tipo de combustivel A ou G').lower()

if tipo == 'a' and litros <= 20:
    total = (litros * 1.9) * 0.97
elif tipo == 'a' and litros > 20:
    total = (litros * 1.9) * 0.95
elif tipo == 'g' and litros <= 20:
    total = (litros * 2.5) * 0.96
elif tipo == 'g' and litros > 20:
    total = (litros * 2.5) * 0.94

print('voce vai pagar no final ', total)