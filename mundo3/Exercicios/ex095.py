'''
Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproeitamento de cada jogador.
'''
campeonato = list()
while True:
    jogador = dict()
    partidas = list()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'quantas partidas o {jogador["nome"]} jogou? '))
    for c in range( 0,tot):
        partidas.append(int(input(f'      Quantos gols na partida {c} ? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    campeonato.append(jogador.copy())
    # print(campeonato)

    resp = str(input('Deseja continuar ? ')).upper()[0]
    if resp in 'nN':
        break

print(f'\tNo. Nome           Gols        Total')
for k,v in enumerate(campeonato):
    print(f'\t{k:<3} {v["nome"]:<14} {v["gols"]} {v["total"]:>5} ')
print('-' * 30)

rsp = int(input('Mostrar dados de qual jogador  ? '))
print(f'-- LEVANTAMENTO DO JOGADOR: {campeonato[rsp]["nome"]}')

for k,v in enumerate(campeonato[rsp]["gols"]):
    print(f'\tNo jogo {k} fez {v} gols')

print("<< VOLTE SEMPRE >>")
'''
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'\tO jogador {k} tem o valor {v} ')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fex {v} gols.')
print(f'Foi um total de {jogador["total"]} gols ')
'''
'''
lista = {}
gols = []
soma = 0

lista['nome'] = str(input('Nome: '))
lista['partidas'] = int(input(f'Quantas partidas {lista["nome"]} jogou? '))
for n in range( 0,int(lista['partidas']) ):
    gols.append( int(input(f'Quantos gols ele fez na {n+1}o. partida: ')) )
    soma += gols[n]

lista['gols'] = gols.copy()
lista['total'] = soma
print('-=' * 30)
print(lista)
print('-=' * 30)
for k, v in lista.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 30)
print( f'O jogador {lista["nome"]} jogou {lista["partidas"]} partidas. ')
for k,v in enumerate(gols):
    print(f'\t=> Na partida {k+1}, fez {v} gol(s). ')

print(f'Foi um total de {lista["total"]} gols.')
'''
