usuarios = list()
senhas = list()
mensagens = []

opcao = 99

while opcao != 0:
    print('-----MENU-----')
    print('1-cadastrar usuario')
    print('2-fazer login')
    print('0-sair')

    opcao = int(input('digite a opcao desejada '))
    if opcao == 1:
        login = input('qual o login do usuario')
        senha = input('qual a senha do usuario')

        if login not in usuarios:
            usuarios.append(login)
            senhas.append(senha)
            mensagens.append('')
            print('usuario cadastrado com sucesso!')
        else:
            print('usuario existente no sistema')
    elif opcao == 2:
        login_user = input('digite seu login')
        senha_user = input('digite sua senha')

        #if usuarios.count(login_user) > 0:
        if login_user in usuarios:
            indice = usuarios.index(login_user)
            if senha_user == senhas[indice]:
                print('login realizado com sucesso')
                opcao2 = 99
                while opcao2 != 0:
                    print('\n---MENU usuario---')
                    print('1-inserir mensagem no diario')
                    print('2-exibir mensagens')
                    print('0-sair da conta')
                    opcao2 = int(input('digite a opcao desejada'))
                    if opcao2 == 1:
                        mensagem = input('digite a mensagem')
                        mensagens[indice] += mensagem + '\n'
                    elif opcao2 == 2:
                        print(f'Mensagens de {login_user}')
                        print(mensagens[indice])


            else:
                print('usuario ou senha incorretos')
        else:
            print('usuario inexistente')

