def dobrar(n=0, formata=False):
    res = n * 2
    return res if formata is False else moeda(res)


def metade(n=0, formata=False):
    res = n / 2
    return res if formata is False else moeda(res)


def aumentar(n=0, a=0, formata=False):
    res = n * (1 + (a/100))
    return res if formata is False else moeda(res)


def diminuir(n=0, a=0, formata=False):
    res = n - (n * (a/100))
    return res if formata is False else moeda(res)


def moeda(valor=0, moeda='RS '):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
