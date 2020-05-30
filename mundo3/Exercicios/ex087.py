'''
Aprimore o desafio anterior, mostrando no final:
- A soma de todos os valores pares digitados
- A soma dos valores da terceira coluna
- O maior valor da segunda linha.
'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = maior = coluna3 = 0

for l in range(0 , 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]

        if c == 2:
            coluna3 += matriz[l][c]

print('-' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

print('-' * 30)
print(f'A soma dos numero da matriz foi: {soma}.')
print(f'A soma dos numeros da coluna 3 foi: {coluna3}.')
print(f'O maior valor digitado na coluna 2 foi: {maior}.')


