#12 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 

sexo = str(input('QUAL SEU SEXO? DIGITE (F) PARA FEMININO E (M) PARA MASCULINO'))
altura = float(input('Qual a sua altura?'))

if sexo == 'F' :
  pesoideal =  (62.1*altura) - 44.7 

elif sexo == 'M':
  pesoideal =  (72.7*altura) - 58

print('Seu peso ideal deve ser:',pesoideal)


