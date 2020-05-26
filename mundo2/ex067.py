# Faça um programa que mostre a tabuada de vários numeros, um de cada vez, para cada valor digitado pelo usuário. O programa sera interrompido quando o número solicitado for negativo
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n <= 0:
        break
    print('-='*30)
    v = 1
    for t in range(1, 11):
        print(f'{v} X {n} = {v*n}')
        v += 1
    print('-='*30)
print('Final do programa')
