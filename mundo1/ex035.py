"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triangulo.
"""
verde = '\033[0;32m'
vermelho = '\033[0;31m'
r1 = int(input('Digite o comprimento da PRIMEIRA reta '))
r2 = int(input('Digite o comprimento da SEGUNDA reta '))
r3 = int(input('Digite o comprimento da TERCEIRA reta '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estes retas \033[0;32mPODEM\033[m formar um triangulo')
else:
    print('Estes retas \033[0;31mNÃO PODEM\033[m formar um triangulo')
