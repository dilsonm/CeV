'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso.'''
extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','desesete','dezoito','dezenove','vinte')
# n = 0
while True:
    n = int(input('Digite um número: '))
    if n >= 0 and n <= 20:
        #n +=1
        break
print('-'*50)
print(f'Você digitou o numero: {extenso[n].upper()}.' )
print('-'*50)
