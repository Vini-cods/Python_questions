'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

Saída esperada:
A dobro de 9 é : 18
A triplo de 9 é : 27
A raiz quadrada de 9 é : 3
'''
numero = int(input('Digite um numero: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5

print(f'o dobro de {numero} é: {dobro}, o triplo de {numero} é: {triplo} e a raiz de {numero} é: {raiz}')