#Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma
'''
for i in range(1, 10 + 1):
    numeros = int(input('Digite um numero por favor: '))

    if numeros % 2 == 0:
        soma = numeros + i
        print(soma)
'''

soma = 0

for i in range(10):
    n = int(input('Numero: '))
    if n % 2 == 0:
        soma = soma + n
        print(f'A soma é {soma}')