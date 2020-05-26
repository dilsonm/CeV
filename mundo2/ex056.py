"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos
"""
from datetime import date
atual = date.today().year
media = 0
nomeh = ""
maisvelho = 0
mulher = 0
for c in range( 0, 4):
    nome = str(input('Digite o nome da pessoa: ')).strip()
    idade = int(input('Digite o ano de nascimento: '))
    sexo = str(input("""Escolha qual é o sexo:
[M] Masculino
[F] Feminino
"""))
    media += (atual - idade)
    if sexo == 'M' and (atual - idade) > maisvelho:
        nomeh = nome
    if sexo == 'F' and (atual - idade) < 20:
        mulher += 1

print('A média de idade das pessoas é: {}'.format(media / 4))
print('O nome do homem mais velho é {}'.format(nomeh))
print('Nesta lista tem {} mulheres com menos de 20 anos de idade.'.format(mulher))
