"""
Desenvolva um programa que pergunte a distancia de viagem em KM.
Calcule o preco da passagem, cobrando R$0,50 por km, para viagens até 200km e
$R0,45 para viagens mais longas.
"""
cores = {
            'limpa':'\033[m',
            'vermelho':'\033[0;31m',
            'azul':'\033[0;34m',
        }
d = int(input("Qual a distancia de sua viagem :"))
if d <= 200:
    print( 'O valor de custo da passagem é: {}{:.2f}{}'.format(cores['vermelho'],d * 0.50,cores['limpa']) )
else:
    print( 'O valor de custo da passagem é: {}{:.2f}{}'.format(cores['azul'],d * .45,cores['limpa']) )
