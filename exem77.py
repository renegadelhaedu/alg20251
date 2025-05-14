#variáveis que representam estruturas de dados são mutáveis dentro
#das funcoes

nome = []
nume = 2

def mudar():
        nome.append('oi')
        nume = 999

mudar()
print(nome)
print(nume)
