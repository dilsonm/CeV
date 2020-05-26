'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou; Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
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
