def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar o número.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    print('-'*tam)


def cabecalho(txt):
    linha()
    # print(f'{txt:^42}')
    print(txt.center(42))
    linha()


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    linha()
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc


def verPessoas():
    cabecalho('Opção 1')

def sair():
    cabecalho('Saindo do Sistema... Até Logo!')
