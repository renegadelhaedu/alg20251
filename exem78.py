pessoas = []
def inserir_pessoa(lista):
        nome = input('digite seu nome')
        lista.append(nome)
        print('pessoa adicionada com sucesso')

op = 99
while op != 0:
        print('1-cadastrar pessoa')
        print('2-listar pessoas')
        print('0-sair')
        op = int(input('digiet a opcao desejada'))
        if op == 1:
                inserir_pessoa(pessoas.copy())
        elif op == 2:
                print(pessoas)
