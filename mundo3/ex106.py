'''
faca um mini-sistema que utilize o interactive  help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: use cores.
'''
c = (
    '\033[m',           # 0 - sem cores
    '\033[0;30;41m',    # 1 - vermelho
    '\033[0;30;42m',    # 2 - verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[7;30m'        # 6 - branco
);

def titulo(msg,cor=0):
    tam = len(msg)+4
    print(c[cor],end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0],end='')

def ajuda(com):
    titulo(f'Acessando o manual do comando {com}',4)
    print(c[6],end='')
    print(help(com))
    print(c[0],end='')


while True:
    titulo('SISTEMA DE HELP byPYTHON',2)
    comando = str(input('Função ou biclioteca > '))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!',2)

'''
# Definicao de cores
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'

ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'

branco = '\033[37m'

restaura = '\033[0;0m'
negrito = '\033[1m'
reverso = '\033[2m'

fpreto = '\033[40m'
fvermelho = '\033[41m'
fverde = '\033[42m'
famarelo = '\033[43m'
fazul = '\033[44m'
fmagenta = '\033[45m'
fciano = '\033[46m'
fbranco = '\033[47m'

#programa principal
titulo = 'SISTEMA DE AJUDA Python'
tam = len(titulo)+4
print(f'{fverde}','~'*tam)
print(f'{titulo:^30}')
print(f'{fverde}','~'*tam)
# print('Veja como ficou a cor')
print(f'{restaura}')
comando = str(input('Função ou biblioteca> '))
tit2 = f"Acessando o manual do comando {comando}"
tam2 = len(tit2)+4
print(f'{fazul}','~'*tam2)
print(f'{tit2:^40}')
print(f'{fazul}','~'*tam2)
print(f'{restaura}')

print(help(comando))
'''
