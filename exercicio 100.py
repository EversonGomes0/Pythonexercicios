from random import randint
from time import sleep
def sorteia(lista):
    #Fazendo uma lista de 5 posições
    for i in range(5):
        lista.append(randint(0, 10))
    print('Sorteando os valores: ', end='')
    for n in lista:
        print(f'{n}', end=' ')
        sleep(0.3)
    print('Pronto!')
    return lista
    #Somando os pares de uma lista
def somapares(lista):
    soma = 0
    print(f'Somando os valores pares de : ',end='')
    for v in lista:
        if v % 2 == 0:
            soma += v
        print(f'{v}', end=' ')
    print (f', temos {soma}')

#Programa principal
numeros = list()
sorteia(numeros)
somapares(numeros)