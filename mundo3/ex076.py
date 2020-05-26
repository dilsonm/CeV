'''Crie um programa que tenha uma tupla unica com nomes de produtos e seus respecctivos precos, na sequencia.
No final mostre uma listagem de preços, organizando os dados em forma tabular'''
lista = ( 'Lapis', 1.75,'Borracha',2,'Caderno',15.9,'Estojo',25,'Transferidor',4.2,'Compasso',9.99,'Mochila',120.32,'Canetas',22.3,'Livro',34.9)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'{lista[pos]:>7.2f}')

print('-'*40)
