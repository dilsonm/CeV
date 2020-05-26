# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
loop = 0
soma = 0
maior = 0 
menor = 99999
conta = 0
while loop != 999:
    n = int(input('Digite um número inteiro qualquer ? '))
    sair = str(input('Deseja continuar [S/N] ? ')).strip().upper()
    if sair == 'S':
        soma += n
        conta += 1
        loop = 999
    else:
        soma += n
        conta += 1

    if n > maior:
        maior = n
    if n < menor:
        menor = n

print( 'A média dos números digitados foi: {}'.format(soma/conta))
print('O maior numero digitado foi: {} '.format(maior))
print('O menor numero digitado foi: {} '.format(menor))
