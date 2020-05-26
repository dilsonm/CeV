'''
Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valore pares e impares. No final mostre os valores pares e impares em ordem crescente.
Ex. [[2,4,6],[3,5,7,9]]'''

lista = []
total = []
pares = []
impares = []

for c in range(0, 6):
    lista.append(int(input('Digite um valor inteiro: ')))

for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

pares.sort()
impares.sort()

total.append(pares[:])
total.append(impares[:])
print(total)
