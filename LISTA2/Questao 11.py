#11 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno =str(input('Digite seu turno, M=MANHA . V = TARDE, N = NOITE') )

if turno == 'm' :
    print('bom dia')

elif turno == 'v' :
    print('boa tarde')

elif turno == 'n' :
    print('boa noite')

else :
    print('invalido')

          
