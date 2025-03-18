num = int(input('digite um numero inteiro'))

if num < 1000:
    centenas = num // 100
    resto100 = num % 100

    dezenas = resto100 // 10
    unidades = resto100 % 10

    print(centenas, 'centenas')
    print(dezenas, 'dezenas')
    print(unidades, 'unidades')
