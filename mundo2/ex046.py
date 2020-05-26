# Faça um programa que mostre na tela uma contagem regressica para o estouro de fogos de artificio, indo de 10 até 0, com uma paisa de 2 segundo entre eles.
import emoji 
from time import sleep
n = 10 
for n in range( n, -1, -1 ):
    sleep(.5)
    print(n)
print('-='*20)
print ( emoji.emojize( ' * Fogos Estourando * :thumbs_up:' ))
