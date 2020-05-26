# """Crie um programa que leia um nome e: 
# Todas as letras maiúscula / 
# Toas as letras minúscula / 
# Quantas letras sem espaço /
# Quantas letras tem o primeiro nome """
nome = input('Digite seu nome completo: ')
#print('Nome digitado: {}'.format(nome))
print('Nome em MAIÚSCULA: {}'.format(nome.upper()))
print('Nome em MINÚSCULA: {}'.format(nome.lower()))
nqtd = len(nome) - nome.count(' ')
print('Este nome tem {} letras sem contas os espaços'.format(nqtd))
n1 = nome.split()
print('O primeiro nome tem {} letras.'.format(len(n1[0])))
