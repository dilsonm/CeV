'''
Crie um programa que leia nome,ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionario receberá tambem o ano de contratação e o salario. Calcule e acrescente, além da idade, com quantoss anos a pessoa vai se aposentar. '''
from datetime import date
dados = dict()

dados['nome'] = str(input('Nome: '))
dados['nasc'] = int(input('Ano de Nascimento: '))
dados['cart'] = int(input('Carteria de Trabalho (0 não tem): '))

anos = date.today().year - dados['nasc']
dados['nasc'] = anos

if dados['cart'] != 0:
    dados['ano'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário R$ '))
    dados['apos'] = dados['nasc'] + ( dados['ano'] + 35 ) - date.today().year

print('-=' * 30)
for k,v in dados.items():
    print(f'{k} tem o valor: {v}')

print('-=' * 30)
print('<< SEJA BEM VINDO >>')
