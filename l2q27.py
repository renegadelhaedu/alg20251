morangos = float(input("Informe o total de KG de morangos: "))
maca = float(input("Informe o total de KG de maça: "))

if morangos <= 5 and morangos >= 0:
    valor_Morango = 2.5 * morangos
else:
    valor_Morango = 1.8 * morangos

if maca <= 5 and maca >= 0:
    valor_Maca = 2.2 * maca
else:
    valor_Maca = 1.5 * maca

valor_pagamento = valor_Maca + valor_Morango
if valor_pagamento > 25 or (morangos + maca) > 8:
    valor_pagamento = valor_pagamento - (valor_pagamento * 0.1)


print(f"O valor a ser pago é R${valor_pagamento}")
