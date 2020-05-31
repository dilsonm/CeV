'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquico de texto simples.
O sistem só vai ter 2 opções: cadastrar uma nova pessoa e listas todas as pessoas cadastradas.
'''
# carregando modulos
from lib.interface import *
from lib.arquivo import *

# programa principal

arq = 'cursoemvideo.txt'
if arquivoExiste(arq):
    print('Arquivo aberto com sucesso')
else:
    print('Arquivo não encontrado.')
    criarArquivo(arq)

while True:
    opc = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])

    if opc == 1:
        verPessoas()
    elif opc == 2:
        cadastrar()
    elif opc == 3:
        sair()
        break
    else:
        print('\033[31mDigite uma opção invalida!\033[m')
