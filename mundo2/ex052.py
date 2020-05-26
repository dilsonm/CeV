# Faça um programa que leia um numero inteiro e diga se ele e ou nao um numero primo
num = int(input('Digite um número: '))
t = 0
for c in range( 1, num + 1 ):
    if num % c == 0:
        t += 1
if t == 2:
    print("Este é um numero PRIMO")
else:
    print('Este NÃO É um número PRIMO !')
