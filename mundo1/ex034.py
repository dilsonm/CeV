"""
Escreva um programa que pergunte o salário de um funcionário e calcule o
valor do seu aumento.
Para salários superiores a R$1.200,00, calcule um aumento de 10%
Para salários inferiores ou iguáis, o aumento é de 15%
"""
n = 'Dilson'
sal = float(input('Informe seu salário:'))
if sal > 1200:
    print('Seu novo salário é : {}{:.2f}{} !!!'.format('\033[0;34m',sal * ( 10 /100) + sal,'\033[m'))
else:   
    print('Seu novo salário é : {}{:.2f}\033[m !!'.format('\033[0;32m',sal * (15/100) + sal))
