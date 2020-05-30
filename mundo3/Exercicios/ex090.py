'''
Faca um programa que leia nome e media de um aluno, guardadando tambem a situação em um dicionario. No final, mpstre o conteudo da estrutura na tela.
E.: Nome=Joao, Média= 4.5, Situação=Reprovado
'''
lista = list()
dic = dict()

dic['nome'] = str(input('Nome: '))
dic['media'] = float(input('Média: '))

lista.append(dic.copy())
print(f'Nome é igual a: {dic["nome"]}')
print(f'Média é igual a: {dic["media"]}')

if float(dic["media"]) > 5:
    print('Situação é igual APROVADO')
else:
    print('Situação é igual REPROVADO')
