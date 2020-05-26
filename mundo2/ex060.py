'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5!=5x4x3x2x1 = 120
'''
c = ''
f = int(input('Digite um número inteiro qualquer: '))
r = 0
sair = 1
for n in range(1, f):
    if n == 1:
        m = n * f
    else:
        m = m * n
    print( n,end='X')

print('{} = {}'.format(f, m)   ) 
