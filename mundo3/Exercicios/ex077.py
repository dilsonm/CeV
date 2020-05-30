'''Crie um programa que tenha uma tupla com varias palavras (não usar acentos). Depois disso, voce deve mostrar, para cada palavra, quais são as suas vogais.'''
lista = ('Sao Paulo','Santos','Praia Grande','Peruibe','Cotia','Jundiai','Araraquara','Valinhos')
vogais = ('a','e','i','o','u')

for c in lista:
    print(f'\n{c:.<30} = ',end='')
    
    for letra in c:
        if letra.lower() in 'aeiou':
            print( letra,end=' '  )

