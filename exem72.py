#funções: blocos de instruções que podem ser chamadas repetidamente
#ajuda a deixar o código compacto
#melhora o reuso de código
#1-funçao que nao tem parametro de entrada e nao tem retorno
#2-funçao que  tem parametro de entrada e nao tem retorno
#3-funçao que  nao tem parametro de entrada e tem retorno
#4-funçao que tem parametro de entrada e tem retorno
def saudar_usuario(nome, idade):
        ano = 2025 - idade
        print(f'ola {nome}, seja bem-vindo. Voce tem apenas {idade} anos')
        print(f'essa pessoa nasceu no ano {ano}')


nome = input('digite seu nome')
idade = int(input('digite sua idade'))
saudar_usuario(nome, idade)







