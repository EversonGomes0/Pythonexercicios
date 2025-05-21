from random import randint
numeros = [randint(0,20) for i in range(5)]
tupla = tuple(numeros)
print (f'Os valores sorteados foram: {tupla}',end= ' ')
print (f'\nO Maior valor foi: {max(numeros)}')
print (f'O Menor valor foi: {min(numeros)}')
