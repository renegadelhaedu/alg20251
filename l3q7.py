#questao 7
maior_lido = 0

for i in range(5):
    numero = int(input('digite um numero'))
    if numero > maior_lido:
        maior_lido = numero

print('o maior numero lido e', maior_lido)