'''
crie um programma que tenha a funcao leiaint(), que vai funcionar de forma semelhante a funcao input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
ex.: n = leiaint('Digite um n')
'''
def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mErro: \033[m por favor digite um número inteiro válido. ')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar um número.')
            return 0
        else:
            return n


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mErro: \033[m por favor digite um número real válido. ')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar um número.')
            return 0
        else:
            return n

# Programa principal
n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real {n2}.')
