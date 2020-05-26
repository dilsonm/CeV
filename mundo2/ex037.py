# Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual a base de conversao: 1) Binario, 2)Octal e 3)Hexadecimal
n = int(input('Digite um numero qualquer: '))
e = int(input('Escolha o modo de conversão: 1-Binário, 2-Octal ou 3-Hexadecimal ' ))

b = bin(n)
o = oct(n)
h = hex(n)

if e == 1:
    print('Você escolheu converter para \033[0;34m BINÁRIO \033[m, o valor é: \033[7m{}\033[m '.format(b))
elif e == 2:
    print('Você escolheu converter para \033[0;34m OCTAL \033[m, o valor é: \033[7m{}\033[m '.format(o))
elif e == 3:
    print('Você escolheu converter para \033[0;34m HEXADECIMAL \033[m, o valor é: \033[7m{}\033[m '.format(h))
else:
    print('Opção selecionada \033[31m NÃO TEM \033[m conversão !')
