import utils as ut


nascimento = input('digite sua data de nascimento no padrao dd/mm/aaaa: ')
while not ut.verificar_data(nascimento):
    print('data informada com erro ')
    nascimento = input('digite sua data de nascimento no padrao dd/mm/aaaa: ')

nome = input('digite seu nome')