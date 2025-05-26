'''
modo de arquivo:
w - cria o arquivo, sobrescrevendo e escreve nele
a - adiciona no final do arquivo

'''

meu_arquivo = open('listaalunos.txt', 'w')

nome = input('diga ai seu nome')

meu_arquivo.write(f'ola, meu nome é {nome}\n')
meu_arquivo.write('\n')
meu_arquivo.write('fala ai meu amigo')
meu_arquivo.close()