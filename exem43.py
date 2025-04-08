candidatos = ['jose','maria','carla']
votos = [0,0,0]

#sao 3400 eleitores

for i in range(5):
    for indice in range(len(candidatos)):
        print(f'vote {indice+1} para votar em {candidatos[indice]}')
    voto = int(input('digite seu voto'))
    votos[voto - 1] += 1

if votos[0] > votos[1] and votos[0] > votos[2]:
    print('quem ganhou a eleicao foi', candidatos[0])
elif votos[1] > votos[0] and votos[1] > votos[2]:
    print('quem ganhou a eleicao foi', candidatos[1])
elif votos[2] > votos[0] and votos[2] > votos[1]:
    print('quem ganhou a eleicao foi', candidatos[2])
else:
    print('vai ter que haver segundo turno')

