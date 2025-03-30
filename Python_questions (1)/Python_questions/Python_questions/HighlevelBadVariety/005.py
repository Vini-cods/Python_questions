'''
Escreva um programa que converta real para o Franco Congolês
Saída esperada:10,00 reais, equivalem a 5052,00 Francos Congoleses
'''

real = float(input('Digite a quantidades de reais a ser convertido: '))

fc = real * 499.45

#print(f'A conversão de R${real} para franco congoles é ${fc:.2f}')
print(f'A conversão de R${real} para franco congoles é ${real * 499.45}')