#read
novo = open('meusatletas.txt', 'r')

linhas = novo.readlines()
novo.close()

for linha in linhas:
    cortada = linha.replace('\n','')
    if 'atletas' not in cortada:
        print(cortada)
