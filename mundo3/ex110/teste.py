'''
107) criar um modulo chamado moeda.py que tenha as funcoes incorporadas aumentar(), diminuir(), dobrar() e metade().
Faça tambemum programa que importe esse módulo e use algumas dessas funções.

108) adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetario formatado.

109) modifique as funções que foram criadas no sesafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

110)
adicione ao modulo moeda.py criado nos desafios anteriores, a função chamada resumo(), que mostre na tela algumas informações geradas pelas funcoes que ja temos no modulo criado ate aqui
'''
# from moeda import dobrar, metade, aumentar, diminuir
import moeda

p = float(input('Digite o preço R$ '))
moeda.resumo(p, 10, 13)
