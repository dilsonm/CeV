'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquico de texto simples.
O sistem só vai ter 2 opções: cadastrar uma nova pessoa e listas todas as pessoas cadastradas.
'''
# carregando modulos
from lib.interface import *
from lib.arquivo import *

# programa principal
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opc = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])

    if opc == 1:
        # Opção de listar o conteúdo do arquivo
        lerarquivo(arq)
    elif opc == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVAO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif opc == 3:
        # Opção de sair do sistema
        sair()
        break
    else:
        # Digitou uma opção errada do menu
        print('\033[31mDigite uma opção invalida!\033[m')
