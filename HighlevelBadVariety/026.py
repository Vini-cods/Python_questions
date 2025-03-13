#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = peso / (altura ** 2)


if imc > 25.5:
    print('Obeso')
elif imc > 18.6:
    print('Normal')
else:
    print('Abaixo do padrão')