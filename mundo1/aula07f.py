#Leia um numero e exibir o valor em metros, centimetros e milimetros
n1 = int(input('Entre com o valor em metros: '))
cm = n1 * 10
mm = n1 * 100
print('Valor em metros: {} valor em centimetros: {} valor em milimetros: {}'.format(n1, cm, mm))
