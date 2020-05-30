'''
Crie um programa onde o usuário digite uma expressão qualquer que use parenteses. Seu aplicativo deverá analisar se a expressão passada esta com os parenteses abertos e fechados na ordem correta.
'''
expr = str(input('Digite uma expressão: ')).strip()
parenA = expr.count('(')
parenB = expr.count(')')

if parenA == parenB:
    print('Esta expressão esta VALIDA.')
else:
    print('Esta expressão esta INVALIDA')

