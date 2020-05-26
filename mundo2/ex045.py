"""Crie um programa que faça o computador jogar JOKENPO com você
1-Pedra
2-Papel
3-Tesoura

1 e 1, 2 e 2, 3 e 3 = Empate
1 e 2 = 2 ganha
1 e 3 = 1 ganha
2 e 3 = 3 ganha
2 e 1 = 2 ganha
3 e 1 = 1 ganha 
3 e 2 = 3 ganha
"""
import random
n = int(input('Digite um númro de 1 a 3: '))
r = random.randint(1,3)
print( "-=" * 20 )
print('Você escolheu o número \033[7m{}\033[m --> '.format(n))
print('O computador escolheu o numero \033[7m{}\033[m --> '.format(r))
print( "-=" * 20 )

if n < 1 and n > 3:
    print('Você digitou um número inválido !!!')
elif n == r:
    print('O resultado foi \033[7m EMPATE \033[m ')
elif (n==1 and r==3) or (n==2 and r==1) or (n==3 and r==2):
    print('O resultado foi \033[7m VOCÊ GANHOU \033[m ')
else:
    print('O resultado foi \033[7m VOCÊ PERDEU \033[m ')
