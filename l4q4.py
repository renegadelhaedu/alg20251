#questao 4

carac = []

for i in range(10):
    letra = input('digite a letra')

contador = 0
for letra in carac:
    if letra not in ['a','e','i','o','u']:
        contador += 1

