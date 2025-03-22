'''
Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa
'''

n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))

opcao = 0

while opcao != 5:
    print('---------------------------')
    opcao = int(input('1. Somar'
                        '\n2. multiplicar'
                        '\n3. Maior'
                        '\n4. Novos Numeros'
                        '\n5. Sair do Programa ------> '))

    print('---------------------------------------')

    if opcao == 1:
        print(f'A soma é {n1 + n2 + n3}')

    elif opcao == 2:
        print(f'A multiplicação é {n1 * n2 * n3}')

    elif opcao == 3:
        if n1 > n2 and n1 > n3:
            print(f'{n1} é o maior')
        elif n2 > n3:
            print(f'{n2} é o maior')
        else:
            print(f'{n3} é o maior')

    elif opcao == 4:
        n1 = int(input('N1: '))
        n2 = int(input('N2: '))
        n3 = int(input('N3: '))

    elif opcao == 5:
        print('Até logo :) ')
    else:
        print('Entrada incorreta')