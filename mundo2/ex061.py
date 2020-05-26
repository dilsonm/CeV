# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, monstrando os 10 primeiros termos da progressão usando a estrutura while
t = int(input('Digite um termo: '))
r = int(input('Digite uma razão: '))
l = 1
x = 1
while l <= 10:
    if l == 1:
        print( '{}'.format(x), end=' -> ')
    else:
        x += r 
        print( '{}'.format(x), end=' -> ')
    l += 1

print('Acabou !')
