# Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e que se encontram no intervalo de 1 até 500
soma = 0
for n in range( 1, 501):
    if  (n % 3) == 0:
        soma += n

print( 'A soma dos números multiplos de 3, no intervalo de 1 - 500 é de: {}'.format(  soma))
