#8 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#o C=5*((F-32)/9).

temperatura = float(input('QUAL A TEMPERATURA A SER CONVERTIDA ?'))

celsius = (5*(temperatura-32)/9)

print('EM CELSIUS A TEMPERATURA É',celsius)
