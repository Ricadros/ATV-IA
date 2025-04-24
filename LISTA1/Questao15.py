#15 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math
    
tamanho = float(input('DIGITE O TAMANHO DA AREA QUE DESEJA PINTAR EM METROS QUADRADOS?'))

litrosdetinta = tamanho / 3 

latas = litrosdetinta / 18

latas = math.ceil(litrosdetinta / 18)

valor = latas * 80 

print('Voce precisara de',latas,'galoes de tinta, o que dar o valor total de',valor)