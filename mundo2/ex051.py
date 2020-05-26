# Desenvolva um progama que leia o primeiro termo e a razão de um PA. no final, mostre os 10 primeiros termos dessa progressão.
t = int(input('Digite um termo: '))
r = int(input('Digite uma razão: '))
x = t + (10-1) * r
for n in range( t, x+t , r):
     print( '{}'.format(n), end=' -> ')
print('Acabou !')
