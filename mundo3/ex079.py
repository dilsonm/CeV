'''
Digite um programa onde o usuario pode digitar varios valores numericos e cadastre-os em uma lista. Caso o numero já exista la dentro, ele não será adicionado., No final, srão exibidos exibido todos os valores unicos digitados, em ordem crescente.
OBS: perguntar se continua, e quando existir o numero avisar que não adicionou.
'''
lista = []

while True:
    num = int(input('Digite um valor '))

    if num not in lista:
        lista.append(num)
    else:
        print(f'Este numero {num} já esta na lista e foi descartado.')

    cont = str(input('Deesja continuar [S]im ou [N]ão ? ')).strip().upper()
    if cont[:1] == 'N':
        break

lista.sort()
print(lista)
