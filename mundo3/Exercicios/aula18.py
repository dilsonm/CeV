galera = []
dado = []
totmai = totmen = 0
for c in range( 0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])   # [:] este simbolos define uma cópia
    dado.clear()

for p in galera:
    if p[1] > 21:
        totmai += 1 
        print(f'{p[0]} e maior de idade.')
    else:
        print(f'{p[0]} e menor de idade.')
        totmen += 1

print('-='*50)
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

