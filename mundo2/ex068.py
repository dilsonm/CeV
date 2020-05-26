# Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele consquistou no final do jogo.
import random
print('-='*50)
print('Vamos jogar PAR ou IMPAR')
print('-='*50)
v = 0
while True:
    comp = random.randint(1,9)
    num = int(input('Digite um número: '))

    esc = ' ' 
    while esc not in 'PI':
        esc = str(input('Escolha par ou impar [P/I] ')).strip().upper()[0]

    s = comp + num
    if esc == 'P':
        if s % 2 == 0:
            v += 1
            print('Você GANHOU')
        else:
            break
    else:
        if s % 2 != 0:
            v += 1
            print('Você GANHOU')
        else:
            break
    print('Vamos jogar novamente...')

print('-'*50)
print('Você PERDEU... FIM DE JOGO')
print('-'*50)
