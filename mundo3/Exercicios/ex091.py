'''
Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatorios. guarde esses resultados em um dicionario. no final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero.
Ex.: O jogador 1 tirou {} ---- 1o lugar {} com {} '''
from random import randint
from time import sleep
from operator import itemgetter

dic = {
        'jogador1':randint(1 , 6),
        'jogador2':randint(1 , 6),
        'jogador3':randint(1 , 6),
        'jogador4':randint(1 , 6)
        }
rank = list()
print('Valores Sorteados...')
for k,v in dic.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

rank = sorted( dic.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('<< Ranking dos Jogadores >>')
for i,v in enumerate(rank):
    print(f'   {i+1}o. lugar: {v[0]} com {v[1]}. ')
    sleep(1)
