'''Crie um programa que leia o nome e o preco de varios produtos. O programa devera perguntar se o usuario vai continuar.
    No final mostre:
    a) Qual é o total gasto na compra 
    b) Quantos produtos custam mais de R$1000. 
    c) Qual é o nome do produto mais barato. '''
sair = 'N'
compras = 0
prdcaro = 0
nomeprd = ''
precomenor = 999999
print('-'*50)
print('Mercado Popular')
print('-'*50)
while sair != 'S':
    prod = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o valor do produto: '))
    while True:
        cont = str(input('Continua comprando ? [S/N] ')).strip().upper()
        if cont == 'S':
            break
        else:
            sair = 'S'
            break
    compras += preco
    if preco > 1000:
        prdcaro += 1
    if preco < precomenor:
        nomeprd = prod
        precomenor = preco
print('='*50)
print(f'O tota de compras foi: {compras}')
print(f'Foi comprado {prdcaro} produro com valor acima de R$1000.')
print(f'O nome do produto mais barato é: {nomeprd}.')
print('='*50)
