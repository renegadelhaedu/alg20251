login = 'renesousa'
senha = 'fafabelem'

tentativa = 1
logado = False
while tentativa <= 5:
    login_user = input('digite seu login')
    senha_user = input('digite sua senha')

    if login_user == login and senha_user == senha:
        logado = True
        break

    tentativa +=1

if logado == True:
    print('voce está logado no sistema')
    print('------MENU-----')
    print('1-comprar produto')
    print('2-comprar produto')
else:
    print('login ou senha incorretos')