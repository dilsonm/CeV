#Crie um programa que lia o nome de uma cidade e diga se ela começa ou nao com o nome "SANTO"
cid = str(input('Qual o nome da sua cidade: '))
print(cid[:3].upper() == 'SÃO')
