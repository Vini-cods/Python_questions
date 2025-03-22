palavra = input('Palava: ').strip().lower()

if palavra == palavra[::-1]:
   print('É palindromo')
else:
  print('Não é')


# pontos = 0

# for i in range(0, len(palavra)):
#   if palavra[i] == palavra[-i -1]:
#     pontos = pontos + 1

# if pontos == len(palavra):
#   print('É um palindromo')
# else:
#   print('Não é')