#14 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a. salário bruto.
#b. quanto pagou ao INSS.
#2
#c. quanto pagou ao sindicato.
#d. o salário líquido.
#e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

trabalho = float(input('Digite quanto voce ganha por hora?'))
horas = int(input('Quantas horas por mes voce trabalha?'))

salario = trabalho * horas

impostoDeRenda = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05

salarioliquido = salario - impostoDeRenda - inss - sindicato

print('Salario Bruto :',salario, '\nImposto de renda :',impostoDeRenda,'\nInss :',inss,'\nSindicato :',sindicato, '\nsalario liquido:',salarioliquido)