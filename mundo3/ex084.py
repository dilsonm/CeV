'''
Faca um programa que leia nome e peso de varios pessoas, guardando tudo em uma lista. No final, mostre:
- Quanta pessoas foram cadastradas.
- Uma listagem com as pessas mais pesadas
- Uma listagem com as pessoas mais leves
Ex.: João 100, Paulo 77 e Maria 88, Edna 88 -> Mais pesado João e menos pesado Maria e Edna '''

lista  = []
princ = []

maior = 0
menor = 999999

while True:
    lista.append(str(input('Nome: ')).strip())
    lista.append(float(input('Peso: ')))
    princ.append(lista[:])
    lista.clear()

    cont = str(input('Deseja continuar ?')).upper()
    if cont[:1] == 'N':
        break

for c in princ:
    if c[1] > maior:
        maior = c[1]

    if c[1] < menor:
        menor = c[1]


print('-='*50)
print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso foi {maior}Kg. Peso de: ',end='' )
for v in princ:
    if v[1] == maior:
        print(f'[{v[0]}] ',end='')

print()
print(f'E o menor peso foi {menor}Kg. Peso de: ',end='')
for v in princ:
    if v[1] == menor:
        print(f'[{v[0]}] ',end='')

''' 
# solução do guanabara 

num = [[],[]]
valor = 0
for c in range(1 , 8):
    valor = int(input(f'Digite o {c}o valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')
'''
