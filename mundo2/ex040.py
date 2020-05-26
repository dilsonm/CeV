"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
- Média abaixo de 5.0 = REPROVADO
- Média entre 5.0 e 6.9 - EM RECUPERAÇÃO
- Média acima de 7 = APROVADO.
"""
n1 = float(input('Digite sua nota da primeira avaliação: '))
n2 = float(input('Digite sua nota da segunda avaliação: '))

m = (n1+n2)/2 

if m < 5:
    print('Sua médio foi {:.2f} e você esta \033[31m REPROVADO \033[m !'.format(m))
elif m > 5 and m < 7:
    print('Sua médio foi {:.2f} e você esta em \033[33m RECUPERAÇÃO \033[m !'.format(m))
else:
    print('Sua médio foi {:.2f} e você esta \033[34m APROVADO \033[m !'.format(m))
