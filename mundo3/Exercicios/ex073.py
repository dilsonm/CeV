'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os ultimos 4 colocados. 
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela esta o time da chapecoense.'''
tabela = ('América-MG','Flamengo','Palmeiras','Corinthians','Atletico-MG','Fluminense','São Paulo','Grêmio','Internacional','Botafogo','Esport','EC Vitoria','Cruzeiro','Santos','Vasco da Gama','Atletico-PR','Bahia','Chapecoense','Ceará','Paraná')
pos = tabela.index('Chapecoense',0,20)+1
# print(pos)
#tabela.index('Chapecoense')
print('-='*60)
print(f'Lista dos 5 primeiros colocados: {tabela[0:5]}')
print('-='*60)
print(f'Lista dos 4 últimos colocados: {tabela[16:]}')
print('-='*60)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-='*60)
print(f'A Chapecoense esta na {pos}a posição.')