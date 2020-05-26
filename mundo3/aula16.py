'''
valores = []
# valores.append(5)
# valores.append(4)
# valores.append(2)
for cont in range( 0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei  ao final !!!')
'''
a = [2,3,4]
#b = a   # lista lincadas, quando muda uma muda na outra
b = a[:]    #copia da lista A, abaixo a linha que muda somente uma das listas
b[2] = 9
print(a)
print(b)
