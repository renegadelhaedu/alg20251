def inserir_arquivo(nome, end, idade):
    arq = open('arquivo.txt', 'a')
    texto = f'nome:{nome};endereco:{end};idade{idade}\n'
    arq.write(texto)
    arq.close()

def buscar_maioridade():
    lista = []
    arq = open('arquivo.txt', 'r')
    linhas = arq.readlines()
    arq.close()

    for linha in linhas:
        idade = int(linha.split('idade')[-1])
        if idade >= 18:
            lista.append(linha)

    return lista

print(buscar_maioridade())




#inserir_arquivo('john weine','rua padre correia,12',17)


