"""
A confederacao nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostra sua categoria de acordo com sua idade:
- Até 9 anos = Mirim
- Até 14 anos = infantil
- Até 19 anos = Junior
- Até 20 anos = Senior
- Acima = Master
"""
ano = int(input('Digite o ano de seu nascimento: '))

cat = (2020 - ano)
print('Categoria: {}'.format(cat))

if (2020 - ano) < 9:
    print('Sua categoria é: \033[7m MIRIM \033[m ')
elif (2020 - ano) > 9 and (2020 - ano) < 14:
    print('Sua categoria é: \033[7m INFANTIL \033[m ')
elif (2020 - ano) > 14 and (2020 - ano) < 19:
    print('Sua categoria é: \033[7m JUNIOR \033[m ')
elif (2020 - ano) >= 19 and (2020 - ano) <= 20:
    print('Sua categoria é: \033[7m SENIOR \033[m ')
else:
    print('Sua categoria é: \033[7m MASTER \033[m ')
