'''
Crie um programa onde o usuario possa digitar 5 valores numericos e cadastre em uma lista, já na posição correta de inserção sem usar o SORT(). No final mostre a lista ordenada na tela.
OBS: Adicionado na posição / final da lista '''
# x = []
# print(len(x))
# print(len(x) > 0)


lista = []

for c in range( 0, 5):
    num = int(input('Digite um numero qualquer: '))

    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print('#'*50)
print(lista)

