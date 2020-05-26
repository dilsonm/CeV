#crie um programa que leia um número de 0 -9999 
# e mostre na tela cada um dos digitos separados
# ex.: 1834 => unidade: 4, dezena: 3, centena: 8 e milhar: 1
numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
