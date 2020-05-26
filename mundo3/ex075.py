'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla, No final,mostre:
a) Quantas vezes apareceu o numero 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.'''
tupla = ( int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')), int(input('Digite ultimo valor: ')), )
print(tupla)
print(f'O numero 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O numero 3 apereceu na {tupla.index(3)+1}a posição.')
else:
    print('O numero 3 não foi digitado!')
print('Os valore paress digitados foram: ' )
for c in tupla:
    if c % 2 == 0:
        print(c,end=' ')