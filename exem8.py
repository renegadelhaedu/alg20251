#desenvolva um algoritmo na linguagem python para ler o peso
#de um carro, o peso dos 3 ocupantes e exibir:
#a soma de pesos dos passageiros e do carro
#a média de pesos apenas dos ocupantes

pesocarro = float(input('digite o peso do carro'))
pesopassag1 = float(input('digite o peso do passageiro 1'))
pesopassag2 = float(input('digite o peso do passageiro 2'))
pesopassag3 = float(input('digite o peso do passageiro 3'))

soma_total = pesocarro + pesopassag1 + pesopassag2 + pesopassag3
media_ocup = (pesopassag1 + pesopassag2 + pesopassag3) / 3

print('a soma total foi'  , soma_total)
print('a média de peso dos ocupantes é ', media_ocup)