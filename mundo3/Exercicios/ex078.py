valores = []
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    maior = max(valores)
    menor = min(valores)


print('-='*50)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posição ',end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}... ',end='')
print()

print(f'O menor valor digitado foi {menor} nas posição ',end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}... ',end='')
print()

print('Cheguei ao final da lista !')