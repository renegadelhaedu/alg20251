times = {'flamengo':21, 'sousa':23,'vasco':20,'abc':45}

auxiliar = dict()

for time in times.keys():
    print(time, ' - ', times[time])
    if times[time] % 2 == 0:
        auxiliar[time] = times[time]

del times


print('Sobrou:')
print(auxiliar)
