'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
 taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
  com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse 
ou iguale a população do país B, mantidas as taxas de crescimento
'''

popA = int(input('qual a populacao de A'))
txA = float(input('digite a taxa de crescimento de A'))
txA = 1 + txA/100
popB = int(input('qual a populacao de B'))
txB = float(input('digite a taxa de crescimento de B'))
txB = 1 + txB/100

anos = 0

while popB > popA:
    anos += 1
    popA = round(popA * txA, 0)

    popB = round(popB * txB, 0)
    print(f'Pop A: {popA} - Pop B: {popB}')

print(f'levou {anos} anos para A superar ou igualar B')















