'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final Mostre:
a) quantas pessoas tem mais de 18 anos
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
'''
maior = 0
homem = 0
mulher = 0
sair = 'N'
while sair != 'S':
    p = str(input('Digite seu nome: ')).strip()
    i = int(input('Digite sua idade: '))
    s = 'X'
    while s not in 'M/F':
        s = str(input('Digite seu sexo [M/F] : ')).strip().upper()
        if s in 'MF':
            break
    if i > 18:
        maior += 1
    if s == 'M':
        homem += 1
    if s == 'F' and i < 20:
        mulher += 1
    
    cont = 'X'
    while cont != 'S':
        cont = str(input('Deseja continuar [S/N] ? ')).strip().upper()
        if cont == 'N':
            sair = 'S'
            break

print('-'*50)    
print(f'Total de pessoas com mais de 18 anos {maior}.')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulher(es) com menos de 20 anos.' )
print('-'*50)
print('F I M')    
