'''
criar um modulo chamado moeda.py que tenha as funcoes incorporadas aumentar(), diminuir(), dobrar() e metade().
Faça tambemum programa que importe esse módulo e use algumas dessas funções.
'''
#from moeda import dobrar, metade, aumentar, diminuir
import moeda

p = float(input('Digite o preço R$ '))
print(f'O dobro do preço {p} é {moeda.dobrar(p)}.')
print(f'A metade do preço {p} é {moeda.metade(p)}.')
print(f'Aumentado em 10%, temos {moeda.aumentar(p,10)}.')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13)}.')
