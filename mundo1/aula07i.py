#Ler a largura e altura da parede e calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que 1l = 2m quadrado
l = int(input('Digite a largura da parede: '))
a = int(input('Digite a altura da parede: '))
ar = l * a
lt = ar / 2
print('Para pintar a area de {} e necessario {} litros de tinta!'.format(ar, lt))
