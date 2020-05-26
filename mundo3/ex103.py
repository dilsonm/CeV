'''
faca um programa que tenha uma funcao chamada ficha(), que receba dois parametros opcionais: o nome de um jjogador e quantos gols ele marcou.
O programa devera ser capaz de mostrar a fucha do joggador, mesmo que algum dado não tenha sido informado corretamente.
'''
def ficha(g):
    global jogador
    if len(jogador.strip()) == 0:
        jogador = '<desconhecido>'

    if g.strip() == '':
        g = 0

    print(f'O Jogador {jogador} fez {g} gols no campeonato')

jogador = str(input('Nome do Jogador: '))
gols = str(input('Numero de gols: '))
ficha(gols)

'''
# SOLUCAO GUANABARA
def ficha(jog='<desconhecido>',gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# Programa principal
n = str(input('Nome do jogador: ' ))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g) 
'''