#Faça um programa que lia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A" / Em que posição ela aparece a primeira vez / Em que posição ela aparece a última vez
frase = str(input('Digite uma frase: ').strip().upper())
print('A letra A aprece: {} vezes'.format(frase.count('A')))
print('A primeira letra aparece na posição: {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição: {}'.format(frase.rfind('A')+1))