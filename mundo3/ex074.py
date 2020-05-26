'''Crie um programa que vai gerar cinco numeros aleatoriamente e colocar em uma tupla.
Depois disso, mostre a listagem de numeros gerados e trambem indique o menor e o maior valor que estao na tupla'''
import random
tupla = ( random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9) )
print(f'Os valores sorteados foram: ')
for c in tupla:
    print(f'{c} ',end=' ')
print(f'\nO maior valor sorteado foi:  {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')

'''
x = ''
maior = -1
menor = 99
for c in range(0,5):
    n = random.randrange(0,9)
    x += str(n)+','
    if n > maior:
        maior = n
    if n < menor:
        menor = n

tupla = x

print(f'Listagem: {tupla}.' )
print( f'Numero MAIOR: {maior}.' )
print( f'Numero MENOR: {menor}.' )
'''
