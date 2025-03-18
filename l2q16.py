a = float(input('digite o valor de a'))
if a != 0:
    b = float(input('digite o valor de b'))
    c = float(input('digite o valor de c'))

    delta = b**2 - 4*a*c
    if delta < 0:
        print('nao possui raizes reais')
    elif delta == 0:
        x1 = (-b + (delta ** (1/2))) / (2 * a)
        print('o valor de x linha é', x1)
    else:
        x1 = (-b + (delta ** (1 / 2))) / (2 * a)
        x2 = (-b - (delta ** (1 / 2))) / (2 * a)
        print('o valor de x linha é', x1)
        print('o valor de x duas linhas é', x2)
