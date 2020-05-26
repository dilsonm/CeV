# Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o ultimo nome
n = str(input('Digite seu nome completo !')).strip()
nome = n.split()
print('Seu primeiro nome é:{}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))
