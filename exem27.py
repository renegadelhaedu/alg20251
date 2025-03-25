# a turma do p1 precisa eleger um representante de sala. a eleição contém
#apenas 3 candidatos para serem votados pelos 55 alunos. Construa um algoritmo
#em python para ler o nome dos 3 candidatos e receber os votos. O programa deve
#informar ao final quem foi o candidato eleito.

#nome1 = input('digite o nome do primeiro candidato')
#nome2 = input('digite o nome do segundo candidato')
#nome3 = input('digite o nome do terceiro candidato')
nome1 = 'rene'
nome2 = 'jose'
nome3 = 'maria'


c1 = 0
c2 = 0
c3 = 0

for i in range(55):
    print('vote 1 para ', nome1, ',vote 2 para',nome2,' e vote 3 para',nome3)
    voto = int(input('digite o voto'))
    if voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1

if c1 > c2 and c1 > c3:
    print(nome1,'foi o grande vencedor da eleicao')

if c2 > c1 and c2 > c3:
    print(nome2,'foi o grande vencedor da eleicao')

if c3 > c2 and c3 > c1:
    print(nome3,'foi o grande vencedor da eleicao')