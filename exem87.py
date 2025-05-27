#read
novo = open('meusatletas.txt', 'r')
linhas = novo.readlines()
novo.close()

ind = linhas.index('rene\n')
linhas[ind] = 'maria joaquina\n'

novo = open('meusatletas.txt', 'w')
novo.writelines(linhas)
#for linha in linhas:
#    novo.write(linha)
novo.close()


