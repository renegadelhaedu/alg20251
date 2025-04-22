pessoas = []

pessoas.append(['rene@gmail.com','12345','rene de sousa'])
pessoas.append(['maria@gmail.com','34534545','maria de deus'])
pessoas.append(['erica@gmail.com','1999','erica nascimento'])
pessoas.append(['crisitina@gmail.com','1999','maria cristina'])

for p in pessoas:
    if 'maria' in p[2]:
        print(p[0])