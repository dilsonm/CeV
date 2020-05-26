"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se e a hora de se alistar ao servico militar
- Se já passou do tempo de alistamento ao serviço militar
(*) Seu programa também devera mostrar quanto tempo falta ou o que passou do tempo
"""
ano = int(input('Digite o ano de seu nascimento: '))

if (2020 - ano) < 18:
    print('Você ainda tem {} anos para se alistar ao seviço militar.'.format( ((2020 - ano)-18)*-1 ))
elif (2020 - ano) == 18:
    print('Você esta no ano para se alistar ao seviço militar.')
else:
    print('Você já tem {} anos passados que deveria se apresentar ao seviço militar.'.format( (2020 - ano )-18 ))
