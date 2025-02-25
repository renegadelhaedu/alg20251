a = int(input('digite um numero'))
b = int(input('digite um numero'))

c = int(input('digite um numero'))

delta = b**2 - 4*a*c
print('o valor de delta é', delta)

x1 = (-b + delta ** (1/2)) / (2*a)
x2 = (-b - delta ** (1/2)) / (2*a)

print('a primeira raiz da equacao é ', x1)
print('a segunda raiz da equacao é ', x2)
