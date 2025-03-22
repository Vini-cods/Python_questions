#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.

import random

pc = random.randint(1, 10)
j = int(input('Digite algo entre 1 e 10: '))

contador = 1
while pc != j:
    j = int(input('Digite algo entre 1 e 10: '))
    contador += 1

    print(f'Parabens!! acertou {pc} com {contador} vezes ')