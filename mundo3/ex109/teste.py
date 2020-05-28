'''
107) criar um modulo chamado moeda.py que tenha as funcoes incorporadas aumentar(), diminuir(), dobrar() e metade().
Faça tambemum programa que importe esse módulo e use algumas dessas funções.

108) adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetario formatado.

109) modifique as funções que foram criadas no sesafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''
# from moeda import dobrar, metade, aumentar, diminuir
import moeda

p = float(input('Digite o preço R$ '))
print(f'O dobro do preço {moeda.moeda(p)} é {moeda.dobrar(p,True)}.')
print(f'A metade do preço {moeda.moeda(p)} é {moeda.metade(p,True)}.')
print(f'Aumentado em 10%, temos {moeda.aumentar(p,10,True)}.')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13,True)}.')
