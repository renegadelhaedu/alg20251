
n1 = float(input('sua primeira nota? '))
n2 = float(input('sua segunda nota? '))
media = (n1 + n2) /2
if media >=7 and media <10:
    print('aprovado')
elif media < 7:
    print('reprovado')
elif media == 10:
    print('aprovado com distinção')
else:
    print('numero invalido')
