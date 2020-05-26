'''
faca um programa que tenha lista chamada numeros e duas funcoes chamadas sorteia() e somapar(). A primeira vai sortear 5 numeros e vai coloca-los dentro de uma lista e a segunda função vai mostra a soma entre todos os valores pares sorteados pela funcao anterior
'''
from random import randint
from time import sleep

def sorteia():
    num = list()
    print(f'Sorteando 5 valores da lista: ',end=' ')
    for c in range( 0, 5):
        num.append(randint(1,10))
        print(f' {num[c]}',end=' ')
        sleep(.5)
    print('PRONTO!')
    return num

somapares = 0
lst = sorteia()
for c in lst:
    if c % 2 == 0:
        somapares += c

print(f'Somando os valores pares de {lst}, temos: {somapares}')
