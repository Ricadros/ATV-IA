#08 - Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
n3 = int(input('Digite o terceiro número'))

maximo = max(n1,n2,n3)
minimo = min(n1,n2,n3)

print('O MENOR NÚMERO É:',minimo,'E O MAIOR É',maximo)
