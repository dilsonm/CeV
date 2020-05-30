'''
Faca um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final, mpostre um boletim contendo a média de cada um e permita que o usúario possa mostrar os notas de cada aluno individualmente.
OBS.: Os dados tem que estar em uma unica lista.
'''
escola = []
cont = 1
while  True:
    aluno = []
    notas = [0,0]

    aluno.append(str(input('Nome: ')))
    notas[0] = float(input('nota 1: '))
    notas[1] = float(input('nota 2: '))

    escola.append([aluno[:],notas[:]])

    cont = str(input("Quer continuar ?")).upper()
    if cont[:1] == 'N':
        break

print('-=' * 20)
print('No. Nome           Média')
print('-'* 24)
for c, v in enumerate(escola):
    media = ( float(escola[c][1][0]) + float(escola[c][1][1]) ) / 2
    print(f'{c+1:<3} {escola[c][0][0]:<15} {media}')

print('-=' * 20)

while True:
    sair = int(input('Mostrar nota de qual aluno, 999 para sair: '))

    if sair == 999:
        break
    else:
        N0 = escola[sair-1][0][0]
        N1 = escola[sair-1][1][0]
        N2 = escola[sair-1][1][1]
        print(f'Notas de  {N0} são: {N1}, {N2};')
