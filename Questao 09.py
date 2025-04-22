#09 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('DIGITE O VALOR DO PRIMEIRO PRODUTO'))
produto2 = float(input('DIGITE O VALOR DO SEGUNDO PRODUTO'))
produto3 = float(input('DIGITE O VALOR DO TERCEIRO PRODUTO'))

valor = min(produto1,produto2,produto3)
print('Voce deve optar pelo produto',valor,'pelo seu custo beneficio, é o que mais vale a pena')