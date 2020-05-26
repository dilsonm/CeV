'''O usuário vai pensar em um numero e o computador vai gerar um aleatório 
entre 1 e 5, depois verifique se acertou ou errou'''
import random
r = random.randint(1,5)
n = int(input('Digite um número inteiro qualquer no intervalo de 1 - 5: '))
if n == r:
    print('Parabens, você acertou!!! {}'.format(n))
print('O numero randomico foi {} '.format(r))
