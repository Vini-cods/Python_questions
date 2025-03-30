#Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.

palavra = input('Digite uma palavra: ')
if palavra[0] == 'a' or palavra[0] == 'e' or palavra[0] == 'i' or palavra[0] == 'o' or palavra[0] == 'u':
    print('Começa com vogal')

else:
    print('Começa com consoante')
