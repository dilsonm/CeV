# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lido.
pesomaior = 0
pesomenor = 1000
for n in range(0, 5):
    peso = float(input('Digite o peso da n pessoa: '))
    if peso < pesomenor:
        pesomenor = peso
    if peso > pesomaior:
        pesomaior = peso
print('O MAIOR peso encontrado foi {:.2f}'.format(pesomaior))
print('O MENOR peso encontrado foi {:.2f}'.format(pesomenor))
