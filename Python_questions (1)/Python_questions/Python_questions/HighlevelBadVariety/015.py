#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

'''

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('Par')
elif numero % 2 == 1:
    print('Ímpar')

'''



numero = input('digite um numero: ')
print(numero[-1])

if numero[-1] == '0':
    print('é par')
elif numero[-1] == '2':
    print('é par')
elif numero[-1] == '4':
    print('é par')
elif numero[-1] == '6':
    print('é par')
elif numero[-1] == '8':
    print('é par')
else:
    print('é impar')

numero = int(input('digite um numero: '))
if numero % 2 == 0:
    print('é par')
else:
    print('é impar')
