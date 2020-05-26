# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre a quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
atual = datetime.date.today().year
maior = 0
menor = 0
for c in range( 0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    if atual - ano < 18:
        menor += 1
    else:
        maior += 1
print('Tivemos {} maior de idade'.format(maior))
print('Tivemos {} menor de idade'.format(menor))
