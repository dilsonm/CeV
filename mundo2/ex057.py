'''Faca um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até que ter um valor correto.'''
sexo = ' '
while sexo not in 'M/F':
    sexo = str(input('Digite o sexo: ')).strip().upper()
print('Fim...')
