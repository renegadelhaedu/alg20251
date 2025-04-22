desafetos = []

resposta = 'sim'

while resposta == 'sim':
    nome = input('digite o nome de uma pessoa que voce nao gosta ')
    end = input('digite o endereço dela ')

    desafetos.append([nome, end])

    resposta = input('digite sim para continuar ou nao para encerrar')

print(desafetos)