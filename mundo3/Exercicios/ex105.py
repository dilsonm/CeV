'''
faca um programa que tenha uma funcao notas() que pode receber várias notas de aluno e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também a docstring da função.
'''
def notas(*num, sit=False ):
    r = dict()
    r['quantidade'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num) / len(num)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

#Programa principal
resp = notas(5.5,9.5,10,6.5, sit=True)
print(resp)
