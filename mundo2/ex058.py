'''
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
import random
r = random.randint(1,10)
n = 0
s = 0
while r != n:
    n = int(input('Digite um número inteiro qualquer no intervalo de 1 - 10: '))
    s += 1
print('Foram necessário {} palpites para o acerto ! '.format(s))
