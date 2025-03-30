'''
Faça um programa que leia um número e retorne o fatorial !

4! = 4 x 3 x 2 x 1

'''

n = int(input('Numero: '))

resultado = 1

while n > 0:
    resultado *= n
    n -= 1

print(f'O resultado é {resultado}')