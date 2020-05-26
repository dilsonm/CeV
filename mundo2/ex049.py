# Refaça o desafio=009, mostrando uma tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR
num = int(input("Digite um número de [1] a [10] para monstar a TABUADA: " ))
tit = "TABUADA"
print("-=" * 10)
print("{0:^20}".format(tit))
print("-=" * 10)
for n in range ( 1, 11):
    print(   '{} X {} = {}'.format(num, n, num * n)   ) 
 
