# Faça um programa que leia três números e mostre na tela qual é o MAIOR e qual é o MENOR
import math
n1 = int(input('Digite um primeiro número: '))
n2 = int(input('Digite um segundo número: '))
n3 = int(input('Digite um terceiro número: '))
cores = {
    'azul':'\033[0;34m',
    'amarelo':'\033[0;33m',
    'vermelho':'\033[0;32m',
    'limpa':'\033[m',
}
if (n1 < n2 and n1 < n3):
    print('Este é o MENOR número: {}{}{}'.format(cores['vermelho'],n1,cores['limpa']))
if (n2 < n1 and n2 < n3):
    print('Este é o MENOR número: {}{}{}'.format(cores['vermelho'],n2,cores['limpa']))
if (n3 < n1 and n3 < n2) :   
    print('Este é o MENOR número: {}{}{}'.format(cores['vermelho'],n3,cores['limpa']))

if (n1 > n2 and n1 > n3):
    print('Este é o MAIOR número: {}{}{}'.format(cores['azul'],n1,cores['limpa']))
if (n2 > n1 and n2 > n3):
    print('Este é o MAIOR número: {}{}{}'.format(cores['azul'],n2,cores['limpa']))
if (n3 > n1 and n3 > n2):
    print('Este é o MAIOR número: {}{}{}'.format(cores['azul'],n3,cores['limpa']))
