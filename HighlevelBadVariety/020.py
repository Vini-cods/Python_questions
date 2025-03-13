#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

idade = int(input('idade: '))
if idade > 16 and idade < 69:

    peso = float(input('peso: '))
    if peso > 50:
        horas_sono = int(input('horas de sono: '))
        if horas_sono > 5:
            consumo_bebida = input('consumiu bebida alcoolica nas ultimas 12 horas?: ')
            if consumo_bebida == 'N':
                print('pode doar')
            else:
                print('não poderia consumir bebida alcoolica! ')
        else:
            print('horas de sono incorretas')
    else:
        print('peso incorreto')
else:
    print('idade incorreta')