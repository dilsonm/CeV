'''
Faca um programa que tenha uma funcao chamada contador(), que receba tres parametros: incio, fim e passo e realize a contagem.
Sei prorama tem que realizar tres contagens ateaves da função criada:
a) De 1 ate 10, de 1 em 1
b) De 10 ate 0, de 2 em 2
c) Uma contagem personalizada.
'''
from time import sleep
def contagem(n):
    print('-='*30)
    print('Contagem de 1 até 10 pulando de 1 em 1')
    for c in range(0,n):
        print(f'{c+1} ',end='')
        sleep(.5)
    print('FIM!')
    
    print('-='*30)
    print('Contagem de 10 até 0 pulando de 2 em 2')
    for c in range( n, 0, -2):
        print(f'{c} ',end='')
        sleep(.5)
    print('0 FIM!')
    print('-='*30)
    print('Agora é a sua vez de personalizar a contagem')

def contper(inc,fim,inte):
    print('-='*30)
    print(f'Contagem de {inc} até {fim} de {inte} em {inte}')
    for c in range(inc,fim+inte,inte):
        if c <= fim:
            print(f'{c} ',end='')
            sleep(.5)
    print('FIM!')


num = 10
contagem(num)
comeco = int(input('Inicio: '))
fim = int(input('Fim: '))
pula = int(input('Intervalo: '))
contper(comeco,fim,pula)
