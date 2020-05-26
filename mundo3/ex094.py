'''
Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cadas pessoa em um dicionario e todos os dicionarios em uma lista. No final, mostre:
- Quantas pessias foram cadastradas
- A média de idade do grupo
- Uma lista com todas as mulheres
-Uma lista com todos as pessoas com idade acima da média.   
'''
lista = []
pessoas = {}
soma = 0
feminino = []
acima = []

while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo M/F: ')).upper()[0]   # pegando so a 1a letra
    pessoas['idade'] = int(input('Idade: '))
 
    soma += pessoas['idade']
    lista.append(pessoas.copy())

    if pessoas['sexo'] == 'F':
        feminino.append(pessoas['nome'])    

    if pessoas['idade'] > 30:
        acima.append(pessoas.copy())

    cont = str(input('Deseja continuar [S/N] ')).upper()
    if cont[:1] == 'N':
        break

print('-=' * 30)
# print(lista)

media = soma / len(lista)
print( f'\t- O grupo tem {len(lista)} pessoas.' )
print(f'\t- A média de idade é de {media:.1f} anos')
print('\t- As mulheres cadastradas foram: ',end='')

for c,v in enumerate( feminino ):
    print(v,end=' ')

print()
print('\t- Lista das pessoas que esta acima da média:')
print()
for v in acima:
    if v['idade'] > 30:
        print(f'nome = {v["nome"] }; sexo = {v["sexo"]}; idade = {v["idade"]}.')
print()
print('-=' * 5, '<< ENCERRADO >>', '-=' * 5)

'''
# SOLUCAO GUANABARA
galera = [] # ou list()
pessoa = {} # ou dict()
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo M/F :')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO, digite apenas F ou M')
    
    pessoa['idade'] = int(input('Idade :'))
    galera.append(pessoa.copy())
    soma += pessoa['idade']
    while True:
        resp = str(input('Deseja continuar?')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO: Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / (len(galera))
print(f'B) A media de idade e de {media:5.2f} anos')
print('C) As mulheres cadastradas foram: ',end='')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}', end=' ')
print()
print('D) Lista das pessoas que estao acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ',end='')
        for k,v in p.items():
            print(f'{k} = {v} ',end='')
        print()
print('<< ENCERRADO >>')
'''