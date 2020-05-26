"""
Escreve um programa para aprovar o emprestimo bancario para compra de uma casa.
O programa vai perguntar o valor do imovel, o salario do comprador e em quantos anos ele quer pagar
Calculo o valor da prestacao mensal, sabendo que ela não pode exceder 30% do valor do salário ou entao o emprestimo sera negado.
"""
v = float(input('Digite o valor do emprestimo: '))
s = float(input("Digite o valor do salário: "))
a = float(input('Digite em quantos anos pretende pagar: '))
p = v / (a * 12)
s2 = s * (30 / 100)
print( 'Valor da prestação sem juros é {:.2f}'.format(p))
print('O Valor de 30% do sálario é: {:.2f}'.format(s2))
if p > s2:
    print('O Financiamento foi \033[0;31m NEGADO\033[m, o valor supera 30% do seu salário ')
else:
    print('Parabéns seu financiamento foi \033[0;32m APROVADO \033[m, siga com o financiamento. ')