#Ler o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e calcule e mostre o comprimento da hipotenusa
import math
comp = float(input('Entre com o valor do comprimento: '))
alt = float(input('Entro com o valor da altura: '))
hipo = math.hypot( comp, alt )
print('O valor da hipotenusa e: {:.2f}'.format(hipo))
