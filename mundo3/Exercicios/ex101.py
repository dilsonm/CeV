'''
Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleicoes
'''
from datetime import date
def voto(a):
    """
    Programa: Funcao que retorna uma mensage de status sobre o voto
    """
    anos = atual - a
    if anos < 16:
        return f'Com {anos} anos: NÃO VOTA'
    elif anos < 18 or anos > 65:
        return f'Com {anos} anos: VOTO OPCIONAL'
    else:
        return f'Com {anos} anos: VOTO OBRIGATÓRIO'

    return r

#Programa principal
atual = date.today().year
print('-' *30)
ano = int(input('Em que ano você nasceu ? '))
print(voto(ano))
