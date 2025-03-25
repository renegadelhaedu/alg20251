#questao 15

atual = 1
anterior = 1
n = int(input('diga qual termo da série de fibo vc quer'))
print(anterior, end=', ')
print(atual, end=', ')

for i in range(n):
    prox = atual + anterior
    anterior = atual
    atual = prox
    print(prox, end=', ')