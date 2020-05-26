"""
Refaço o exercicio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
- Equilátero = os 3 lados iguais
- Isósceles = 2 lados iguais
- Escaleno = todos os lados diferentes
"""
r1 = float(input('Digite o comprimento da PRIMEIRA reta '))
r2 = float(input('Digite o comprimento da SEGUNDA reta '))
r3 = float(input('Digite o comprimento da TERCEIRA reta '))

res = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2

if res == True:
    print('Estes retas \033[7mPODEM\033[m formar um triangulo')
    if r1 == r2 and r1 == r3:
        print('Este triangulo é um \033[7m EQUILÁTERO \033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Este triangulo é um \033[7m ISÓSCELES \033[m')
    else:
        print('Este triangulo é um \033[7m ESCALENO \033[m')
else:
    print('Estes retas \033[7mNÃO PODEM\033[m formar um triangulo')
