usuarios = list()
senhas = list()

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
        usuarios.append(login)
        senhas.append(senha)
        print('usuario cadastrado com sucesso!')
    elif opcao == 2:
        login_user = input('digite seu login')
        senha_user = input('digite sua senha')
        if usuarios.count(login_user) > 0:
            indice = usuarios.index(login_user)
            if senha_user == senhas[indice]:
                print('login realizado com sucesso')
            else:
                print('usuario ou senha incorretos')
        else:
            print('usuario inexistente')

