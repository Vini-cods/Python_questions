#Operações matemáticas
'''
print (8 + 9) mais
print(5000 - 500) menos
print(59 * 10000) vezes
print(57 / 6) divisão
print(4 ** 245) exponenciação
Três aspas simples cria um comentario geral

#print formatado (contas)
#aspas simples igual javascript

#print formatado (texto)

print('Olá Mundo!!')

#print formatado (texto + variavel)
#o f é para localizar a variavel

idade = 45
print (idade)
print(f'Sua idade é {idade}')

#leitura de dados
nome = input('Digite seu nome: ')
idade = input('Digite a sua idade: ')
print(f'Seu nome é {nome}, e você tem {idade} anos')

#float flutuante
#int para numero inteiro

#tipos de dados
idade_1 = int(input('Digite a primeira idade: '))
idade_2 = int(input('Digite a segunda idade: '))

soma_idade = idade_1 + idade_2

print(f'A soma de idades é : {soma_idade}')
'''


'''
#strings

Senai = 'Luis Eulalio'
print(Senai[0])
print(Senai[3:7])
print(Senai[:5])
print(Senai[7:])

#Analise
print(len(Senai))#quantas letras ao todo
print(Senai.count('i')) #Frequencia de termos
print(Senai.find('E')) #Posição do termo

#Senai = Senai.upper()
print(Senai.upper())
print(Senai.lower())
print(Senai.replace('L', 'P'))
print(Senai)

nome = input('Nome: ').string()
print(nome)


altura = float(input('Altura: '))
if altura > 1.2:
    print('Alto')


#for (laços de repetição)

for i in range(1, 10):
    print ('*')

for i in range(1, 10):
    print(i)

for i in range(10, 1, -1):
    print(i)



#soma de numeros
soma = 0

for i in range(0, 10):
    n = int(input('Numero: '))
    soma = soma + n
    print(soma)

'''