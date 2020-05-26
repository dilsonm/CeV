"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal, e condiçoes de pagamento:
- A vista dinheiro / cheque = 10% de desconto
- A vista no cartão = 5% de desconto
- Em até 2x no cartão = preço normal
- 3x ou mais no cartão = 20% de juros
"""
preco = float(input('Digite o valor do produto: '))
pagto = int(input('Escolha a forma de pagamento: 1)A Vista, 2)1x no Cartão, 3)2x no Cartão ou 4)3x ou mais no Cartão: '))

if pagto == 1:
    print('O valor do produto saiu por: R${:.2f}, considerando 10% de desconto'.format( preco * .90 ))
elif pagto == 2:
    print('O valor do produto saiu por: R${:.2f}, considerando 5% de desconto'.format( preco * .95 ))
elif pagto == 3:
    print('O valor do produto saiu por: R${:.2f}, ou seja, preço normal!'.format( preco ))
else:
    print('O valor do produto saiu por: R${:.2f}, considerando 20% de juros para o parcelamento!'.format( preco * 1.2 ))
