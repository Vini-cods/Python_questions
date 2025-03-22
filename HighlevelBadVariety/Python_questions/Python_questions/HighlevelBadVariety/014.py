#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

numero = int(input('Digite um número negativo ou positivo: '))

if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('Não é um número')