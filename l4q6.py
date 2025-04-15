medias = []

for aluno in range(10):
    soma = 0
    for nota in range(4):
        nota = float(input('digite sua nota '))
        soma = soma + nota
    media = soma / 4
    medias.append(media)

qtdeAprov = 0
for media in medias:
    if media >= 7:
        qtdeAprov += 1

print(f'a quantidade aprovador foi {qtdeAprov}')