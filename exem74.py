#1-funçao que nao tem parametro de entrada e nao tem retorno
#2-funçao que  tem parametro de entrada e nao tem retorno
#3-funçao que  nao tem parametro de entrada e tem retorno
#4-funçao que tem parametro de entrada e tem retorno

def mostrar_resultado(nota1, nota2, nota3):
        media = (nota1 + nota2 + nota3) / 3
        media = round(media, 1)
        return media


minha_media = mostrar_resultado(8.1, 4, 7.9)
print(minha_media)

