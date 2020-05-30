'''
Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disse mostre:
a) Quantos números foram digitados.
b) A lista ordenada em forma decrescente
c) Se o valor 5 foi digitado e se esta ou nao na lista
OBS: Voce digitou {} valores, Os valores em order decrescente são: {}, O valor 5 (não) foi encontrado na lista'''
lista = []
qtd = 0

while True:
    num = int(input('Digite um número inteiro qualquer: '))
    lista.append(num)
    qtd += 1

    cont = str(input('Deseja continuar [S]im ou [N]ão ?')).upper()
    if cont[:1] == 'N':
        break

lista.sort(reverse=True)
print('-='*50)
print(f'Você digitou {qtd} numeros.')
if 5 in lista:
    print('O numero 5 foi digitado.')
else:
    print('O numero 5 não foi digitado.')

print(lista)
print('-='*50)

print()
