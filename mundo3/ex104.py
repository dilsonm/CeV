'''
crie um programma que tenha a funcao leiaint(), que vai funcionar de forma semelhante a funcao input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
ex.: n = leiaint('Digite um n')
'''
def leiaint(txt):
    while True:
        n = str(input(txt))
        if n.isnumeric():
            return int(n)
        else:
            print('ERRO! Digite um número inteiro válido.')

# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
