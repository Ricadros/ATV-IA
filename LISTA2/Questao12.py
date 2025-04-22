#12 -  As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#o Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#o salários até R$ 280,00 (incluindo) : aumento de 20%
#o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela: o o salário antes do reajuste;
#o o percentual de aumento aplicado;
#o o valor do aumento;
#4
#o o novo salário, após o aumento.

salario =float (input('Digite o seu salário :'))

if salario <= 280 :
 salario20 = salario*0.20
 print('O seu salário obteve um aumento de 20%, o que lhe gera um aumento de :',salario20)
    
elif salario >= 281 and salario <= 699 :
 salario15 = salario*0.15 
 print('O seu salário obteve um aumento de 15%, o que lhe gera um aumento de :',salario15)
 
elif salario >= 700 and salario <= 1499 :
 salario10 = salario*0.10 
 print('O seu salário obteve um aumento de 10%, o que lhe gera um aumento de :',salario10)

elif salario >=1500 :
 salario05 = salario*0.05
 print('O seu salário obteve um aumento de 5%, o que lhe gera um aumento de :',salario05)



 
 


