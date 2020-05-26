n1 = int(input('Entre com o valor ? '))
n2 = int(input( 'Outro valor ? '))
s = n1 + n2 
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A some e {} o produto e {} o resultado e : {:.3f}'.format(s, m, d))
print('Divisao inteira {} e potenciacao {}'.format(di, e))
#print sem quebrar a linha
print('A soma é {} o produto e {} o resultado e {:.3f}'.format(s, m, d),end=' --> ')
print('divisao inteira {} e potencia e {}'.format(d, e))
#print quebrar texto
print('Vamos quebrar \n a linha' )