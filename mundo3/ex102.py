'''
crie um programa qye tenha uma funncao fatorial() que receba dois paramnetros: o primeiro que indique o numero a calcular e o outro chamado show, que sera um valor lógico(opcional) indicando se sera mostrado ou nao na tela o processo de calculo do fatorial.
'''
def fatorial(num,show=False):
    """
    -> Calcula o fatorial de um numero
    :param n: numero que sera feito o FATORIAL
    :param show: parâmetro que define se mostra o calculo ou não
    """
    s = num
    for c in range(num, 0, -1):
        if c > 1:
            s = s * (c-1)
        if show:
            print(f'{c}x',end='' )
    print(f' = {s}')

num = int(input('Digite um numero: '))
fatorial(num,True)
help(fatorial)