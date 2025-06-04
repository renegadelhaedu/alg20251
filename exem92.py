import time
antes = time.time()


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

#print(fibonacci(150))
depois = time.time()
print(depois - antes)
'''

n1 = 1
n2 = 2
print(n1)
print(n2)
for i in range(150):
    prox = n2 + n1
    n1 = n2
    n2 = prox
    print(prox)

'''

