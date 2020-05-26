'''
Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disse crie 2 listas extras que vão conter apenas os valore pares e os valores impares digitados, respectivamente.
Ao final mostre o conteúdo das 3 listas. 
OBS: A lista completa é:, A lista de pares é:, A lista de impares é: '''

lista = []
listaP = []
listaI = []

while True:
    
    lista.append(int(input('Digite um número inteiro qualquer: ')))
    cont = str(input('Deseja continuar [S]im ou [N]ão ?')).upper()

    if cont[:1] == 'N':
        break

for v in lista:
    if v % 2 == 0:
        listaP.append(v)
    else:
        listaI.append(v)


print('-='*50)
print(f'A lista completa é: {lista}')
print(f'A lista de PARES é: {listaP}')
print(f'A lista de IMPARES é: {listaI}')
