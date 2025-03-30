#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos



for i in range(7):
    peso = float(input('Digite o peso: '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
            print(f'O maior peso é: {maior} \n'
                  f'O menor peso é: {menor}')
'''

maior_peso = 0
menor_peso = 9999999999999999999

maior_peso = None
menor_peso = None
for i in range(7):
    peso = float(input('Peso: '))

    if menor_peso == None and maior_peso == None:
        maior_peso = peso
        menor_peso = peso

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

        print(f'O maior peso é: {maior_peso} \n'
              f'O menor peso é: {menor_peso}')
'''