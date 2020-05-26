'''
faca um progra,a que tenha uma funcao chamad area(), que receba as dimensoes de um terreno retangular (largura e comprimento) e mpstre a area do terrano. '''
def area(l,c):
    ar = c * l
    print(f'A áre de um terreno {l}m X {c}m é de: {ar}m²')

print(f'{"controle de Terrenos":^30}')
print('-'*30)
larg = float(input('Digite a largura do terrano: '))
comp = float(input('Digite o comprimento do terrono: '))

area(larg,comp)

