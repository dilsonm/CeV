'''
Crie um programa que leia dois valores e mostre na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
n = 0
while n != 5:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n3 = int(input('''Escolha uma das opções: 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa
    '''))
    if n3 == 1:
        r = n1 + n2
    elif n3 == 2:
        r = n1 * n2
    elif n3 == 3:
        r = n1
        if n1 < n2:
            r = n2
    
    if n3 != 4:
        n = 5

print('O resultado conforme sua escolha foi: {:.2f}'.format(r))
