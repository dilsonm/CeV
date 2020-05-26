"""
Crie um programa que leia um numero qualquer e mostre na tela se ele é
par ou impar
"""
n = int(input("Digite um número qualquer "))

if (n % 2) == 0:
    print('Você digitou um numero \033[0;34mPAR\033[m!')
else:
    print('Você digitou um número \033[0;32mIMPAR\033[m')
    