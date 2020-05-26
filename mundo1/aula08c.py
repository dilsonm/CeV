#Ler um angulo qualquer e mostre na tela o valor do seno,  cosseno e tangente do angulo
import math
ang = int(input('Entre com o valor do angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O angulo de: {}\nSENO:{:.2f}  \nCOSSENO:{:.2f}  \nTANGENTE: {:.2f}'.format(ang, sen, cos, tan))
