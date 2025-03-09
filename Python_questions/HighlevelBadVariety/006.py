'''
Escreva um programa que leia 6 notas diferentes e faça a média do aluno
Saída esperada:A sua média final é : 5
'''
nota_1 = float(input('Essa nota é : '))
nota_2 = float(input('Essa nota é : '))
nota_3 = float(input('Essa nota é : '))
nota_4 = float(input('Essa nota é : '))
nota_5 = float(input('Essa nota é : '))
nota_6 = float(input('Essa nota é : '))


media = nota_1 + nota_2 + nota_3 + nota_4 + nota_5 + nota_6 / 6
print(media)
print(f'A sua média é {media}')