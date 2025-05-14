pessoas = list()

def verificar_nome(nome):
        if '@' in nome or '.' in nome:
                return False
        else:
                return True

def verif_idade(idade):
        if idade > 0 and idade < 120:
                return True
        else:
                return False

def ler_dados_user():
        nome = input('digite seu nome')

        while not verificar_nome(nome):
                nome = input('digite seu nome')

        idade = int(input('digite sua idade'))
        while not verif_idade(idade):
                idade = int(input('digite sua idade'))

        pessoas.append([nome, idade])


ler_dados_user()
