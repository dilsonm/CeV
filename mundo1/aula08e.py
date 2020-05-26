#faca um programa que leia o nome dos 4 alunos e depois sorteie a ordem de apresentacao
import random
a1 = input('Preencha o nome do 1o aluno: ')
a2 = input('Preencha o nome do 2o aluno: ')
a3 = input('Preencha o nome do 3o aluno: ')
a4 = input('Preencha o nome do 4o aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('Segue lista de ondem de apresentacao:')
print(lista)
