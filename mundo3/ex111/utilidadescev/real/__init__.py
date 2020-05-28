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


def resumo(preco, taxa, aumento):
    print('-'*50)
    print(f'{"RESUMO DE VALOR":^50}')
    print('-'*50)
    print(f'{"Preço analisado:":<20} {moeda(preco):>15}')
    print(f'{"Dobro do preço:":<20} {dobrar(preco,True):>15}')
    print(f'{"Metade do preço:":<20} {metade(preco,True):>15}')
    print(f'{taxa}{"% de aumento:":<18} {aumentar(preco,taxa,True):>15}')
    print(f'{aumento}{"% de Redução:":<18} {diminuir(preco,taxa,True):>15}')


if __name__ == "__main__":
    resumo(100, 15, 20)
