#1-funçao que nao tem parametro de entrada e nao tem retorno
#2-funçao que  tem parametro de entrada e nao tem retorno
#3-funçao que  nao tem parametro de entrada e tem retorno
#4-funçao que tem parametro de entrada e tem retorno

def mostrar_resultado():
        nota1 = float(input('digite sua primeira nota'))
        nota2 = float(input('digite sua segunda nota'))
        nota3 = float(input('digite sua terceira nota'))
        media = (nota1 + nota2 + nota3) / 3
        media = round(media, 1)
        return media


print(mostrar_resultado())

