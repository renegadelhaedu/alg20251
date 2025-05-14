nome = 'joelderson keven soares da silva'

#print(nome[0:12])

nome_completo = nome.split(' ')
print(nome_completo)

iniciais = ''

for nome in nome_completo:
    if nome not in ['da', 'de', 'dos']:
        iniciais += nome[0]

print(iniciais)