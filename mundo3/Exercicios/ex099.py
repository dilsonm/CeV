'''
Faca um programa que tenha uma funcao chamada maior(), que receba varios parametros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles e o maior.
'''
def maior(lst):
    numaior = max(lst)
    print(f'O maior numero foi: {numaior}')

numeros = []
while True:
    param = int(input('Digite um numero inteiro: '))
    numeros.append(param)
    print(numeros)

    resp = str(input('Deseja continuar? ')).upper()[0]
    if resp in 'N':
        maior(numeros)
        break

print('FIM!')
