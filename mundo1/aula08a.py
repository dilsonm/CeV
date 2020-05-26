#Crie um programa que leia um numero real qualquer e mostre na tela a sua porcao inteira
#import math
from math import trunc
n1 = float(input('Digite um numero: '))
r = trunc(n1)
print( 'A porcao inteira do numero {} e {}'.format(n1, r) )
