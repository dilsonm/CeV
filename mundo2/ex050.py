# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere.
soma = 0
for n in range( 1, 7):
    dig = int(input('Digite o {}o Numero :'.format(n)))
    if dig % 2 == 0:
        soma += dig
print('A soma dos numeros pares é: {}'.format(soma))
 