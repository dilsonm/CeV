'''
faca um programa que tenha uma funcao chamada escreva(), que receba um texto qualquer como parametro e mostre auma mensagem com tamanho adaptavel.
x.: escreva('Olá Mundo!)
saida: 
-------------
Olá Mundo?
-------------
'''
def mensagem(txt):
    tam = len(txt) + 4
    print('-' * tam)
    # print(f'{txt:^len(txt)}')
    print(f'  {txt}')
    print('-' * tam)

t = str(input('Digite seu texto: '))
mensagem(t)
# mensagem('Dilson Mascarenhas')