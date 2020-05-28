def dobrar(n=0):
    res = n * 2
    return res


def metade(n=0):
    res = n / 2
    return res


def aumentar(n=0, a=0):
    res = n * (1 + (a/100))
    return res


def diminuir(n=0, a=0):
    res = n - (n * (a/100))
    return res


def moeda(valor=0, moeda='RS '):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
