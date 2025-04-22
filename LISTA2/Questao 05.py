#05 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra')
if letra in 'aeiou' :
    print('é uma vogal')
else:
    print('é uma consoante')