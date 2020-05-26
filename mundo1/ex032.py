# Faça um programa que leia um ano qualquer e mostre na tela se é BISSEXTO
ano = int(input('Digite um ano qualquer: '))
if (ano % 4) == 0:
    print('Este ano é \033[0;31;42mBISSEXTO\033[m !')
else:
    print('Este ano \033[0;31mNÃO\033[m é \033[0;32mBISSEXTO\033[m !')
