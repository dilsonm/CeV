# num = [1,2,3,4,5]
# num[2] = 9
# num.append(7)
# num.sort() #num.sort(reverse=True)
# num.insert(6,0)
# num.pop()   # elimina o ultimo elemento da lista
# print(num)
# if 4 in num:
#     num.remove(4)
# else:
#     print('Não achei o numero 8')
# print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor: {v}.')
print('Cheguei ao final da lista.')
