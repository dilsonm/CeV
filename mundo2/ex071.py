'''Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuário qual será o valor a ser sacado (numero inteiro) e  o programa vai informar quantas cedulas de cada valor serão entregues.
OBS: Considere que o caixa possúi cédulas de R$50, R$20, R$10 e R$1. '''
n1 = 0
n2 = 0
n3 = 0
n4 = 0
valor = int(input('Digite o valor que quer sacar: '))
while valor != 0:
    if valor >= 50:
        n1 += 1
        valor -= 50
    elif valor >= 20:
        n2 += 1
        valor -= 20
    elif valor >= 10:
        n3 += 1
        valor -= 10
    elif valor >= 1:
        n4 += 1
        valor -= 1

print('-='*50)
print(f'Foram entregues {n1} notas de R$50, {n2} de R$20, {n3} de R$10 e {n4} de R$1. ')
print('-='*50)
