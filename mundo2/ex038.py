"""
Escreva um programa que leia dois numeros inteiros e compare-os, monstrando na tela uma mensagem: 
1) O primeiro valor é maior 
2) O segundo valor é maior  
3) nao existe valor maior, os dois são iguais
"""
n1 = int(input('Digite um numero inteiro : '))
n2 = int(input('Digite outro numero inteiro : '))
if n1 > n2:
    print('O primeiro Valor é \033[32m MAIOR \033[m')
elif n2 > n1:
    print('O segundo Valor é \033[32m MAIOR \033[m')
else:
    print('Não existe valor maior os dois são \033[32m IGUAIS \033[m')
