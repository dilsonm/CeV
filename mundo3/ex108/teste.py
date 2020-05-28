'''
107) criar um modulo chamado moeda.py que tenha as funcoes incorporadas aumentar(), diminuir(), dobrar() e metade().
Faça tambemum programa que importe esse módulo e use algumas dessas funções.
108) adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetario formatado.
'''
# from moeda import dobrar, metade, aumentar, diminuir
import moeda

p = float(input('Digite o preço R$ '))
print(f'O dobro do preço {moeda.moeda(p)} é {moeda.moeda(moeda.dobrar(p))}.')
print(f'A metade do preço {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
print(f'Aumentado em 10%, temos {moeda.moeda(moeda.aumentar(p,10))}.')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p,13))}.')
