#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

'''
for i in range(1, 11):
  print(f'5 x {i} = {5*i}')
'''

numero = int(input('Numero: '))

for i in range(1, 11):
  print(f'{numero} x {i} = {numero * i}')