# Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag
loop = 0
soma = 0
while loop != 999:
    n = int(input('Digite um número inteiro qualquer ? '))
    sair = str(input('Deseja continuar [S/N] ? ')).strip().upper()
    if sair == 'S':
        soma += n
        loop = 999
    else:
        soma += n
print( 'A soma dos números digitados foi: {}'.format(soma))
