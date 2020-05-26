"""
Desenvolva uma lógica, que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
- Abaixo de 18.5 = Abaixo do peso
- Acima 18 e  menor ou igual a 25 = Peso ideal
- Acima 25 e menor ou igual a 30 = Sobrepeso
- Acima de 30 e menor ou igual a 40 = Obesidade
- Acima de 40 = obesidade morbida
"""
p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = p / (a ** 2)
if imc <= 18.5:
    print('Seu IMC {:.2f} esta categorizado como: Abaixo do peso.'.format(imc))
elif imc >18.5 and imc <=25:
    print('Seu IMC {:.2f} esta categorizado como: Peso Ideal.'.format(imc))
elif imc >25 and imc<=30:
    print('Seu IMC {:.2f} esta categorizado como: Sobrepeso.'.format(imc))
elif imc>30 and imc<=40:
    print('Seu IMC {:.2f} esta categorizado como: Obesidade.'.format(imc))
else:
    print('Seu IMC {:.2f} esta categorizado como: Obesidade Morbida!'.format(imc))
