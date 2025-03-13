'''
Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

V = (4/3) . π . r³
A = 4 . π . r²

Saída esperada:

Volume da Esfera: Y
Área da esfera: X
'''

raio = float(input('Digite o raio: '))

v = (4/3) * 3.1415 * raio ** 3
a = 4 * 3.1415 * raio ** 2

print(f'Volume da esfera: {v:.2f}\nÁrea da Esfera: {a:.2f}')