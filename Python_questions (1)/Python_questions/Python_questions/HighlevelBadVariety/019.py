#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.


numero = int(input('Digite um número: '))
if numero >= 0 and numero <= 10:
    print('Entre 0 e 10')
elif numero > 10 and numero <= 20:
    print('Entre 10 e 20')
elif numero > 20:
    print('Maior que 20')
else:
    print('Negativo')