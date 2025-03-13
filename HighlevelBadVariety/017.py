#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

letra = input('Digite uma letra: ').strip().lower()[0]

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Vogal')
else:
    print('Consoante')


# Tudo o que estiver no in pelos '' vira uma sring

if letra in 'aeiou':
    print('Vogal')
else:
    print('Consoante')