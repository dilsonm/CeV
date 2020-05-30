'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
OBS.: usar sleep para apresentar a lista 
Ex.: [4,8,22,32,18,23]
     [12,9,15,44,60,10]
'''
from random import randint
from time import sleep

print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
jogos = []
qtd = int(input('Quantos jogos deseja fazer: ?'))
print(f'"AGUARDE... SORTEANDO {qtd} JOGOS."')
for c in range( 1, qtd+1):
    for x in range(0,6):
        jogos.append(randint(1,60))

    print(f'Jogo No.{c} : {jogos[1:7]}')
    jogos.clear()
    sleep(.5)
print('-' * 7, f'{"< BOA SORTE > "}','-' * 7)

