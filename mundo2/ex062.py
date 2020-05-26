# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
t = int(input('Digite um termo: '))
r = int(input('Digite uma razão: '))
x = 1
sair = 999999
while sair != 0:
    if x == 1:
        print( '{}'.format(x), end=' -> ')
    else:
        print( '{}'.format(x), end=' -> ')
    continua = str(input('Continua mostrando termo? [S/N]')).strip().upper()
    if continua == 'N':
        sair = 0
    else:
        x += r 

print('Acabou !')
