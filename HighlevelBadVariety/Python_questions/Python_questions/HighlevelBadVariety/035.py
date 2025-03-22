'''
Escreva um programa que leia o
 Nome, idade e sexo de 4 pessoas. No final mostre:

 A média de idade do grupo
 Qual é o homem mais velho
 Quantas mulheres têm menos de 20 anos
'''

soma_idades = 0
quant_mulheres_menor_20_anos = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''

#1
for i in range(4):
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()[0]

    soma_idades += idade/4

#2
if sexo == 'm' and idade > idade_homem_mais_velho:
    idade_homem_mais_velho = idade
    nome_homem_mais_velho = idade

#3
if sexo == 'F' and idade < 20:
    quant_mulheres_menor_20_anos += 1


