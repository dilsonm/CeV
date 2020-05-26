# Crie um programa que leia uma frase qualquer e diga se ele é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range( len(junto)-1, -1, -1):
    inverso += junto[c]

if inverso == junto:
    print('A frase é um PALINDROMO')
else:
    print('A frase NÃO é um PALINDROMO')