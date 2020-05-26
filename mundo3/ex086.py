'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta. 
E.: [1][2][3]
    [4][5][6]
    [7][8][9]
'''
'''
mtz1 = []
mtz = []
valor = 0
for c in range(1, 10):
    valor = int(input(f'Digite o {c} valor.'))
    mtz.append(valor)

print('-'*30)
print(f'{" MATRIZ ":^30}')
print('-'*30)
for c in range(0, len(mtz)):
    mtz1.append( [mtz[c]] )
    if len(mtz1) % 3 == 0:
        print(mtz1[c],end='')
        print()
    else:
        print(mtz1[c],end='')
'''
# Solucao do guanabara
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0 , 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
print('-' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
