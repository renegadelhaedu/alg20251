r1 = input("Telefonou para a vítima?").lower()
r2 = input("Esteve no local do crime?").lower()
r3 = input("Mora perto da vítima?").lower()
r4 = input("Devia para a vítima?").lower()
r5 = input("Já trabalhou com a vítima?").lower()
contagem = 0

if r1 == 'sim':
    contagem = contagem + 1
if r2 == 'sim':
    contagem = contagem + 1
if r3 == 'sim':
    contagem = contagem + 1
if r4 == 'sim':
    contagem = contagem + 1
if r5 == 'sim':
    contagem = contagem + 1

if contagem < 2:
    print('voce é um inocente')
elif contagem == 2:
    print('voce é suspeito')
#elif contagem == 3 or contagem == 4:
elif contagem >= 3 and contagem <= 4:
    print('voce é cumplice')
elif contagem == 5:
    print('voce é assassino')