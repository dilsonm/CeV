"""
Ex.: 29 
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km p/hora. mostre uma mensagem dizendo que ele
foi multado.
A multa vai custar R$7,00 por cada KM acima do limite
"""
v = int(input('Qual velocidade do seu carro: '))
if v > 80:
    print('Você foi multado em R${:.2f}'.format( (v-80)*7 ))
