# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (deconsiderando o flag)
n = s = c = 0
while n != 999:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A quantidade de numeros digitados foi {c} e a soma dos números é {s}.')
