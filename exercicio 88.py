from random import randint
from time import sleep
lista = list()
jogos = list()
tot = 1
print('-=-' * 30)
print('Jogo da Mega Sena') #Fazendo o jogo da Megasena com listas
print('-=-' * 30)
quant = int(input('Quantos jogos você vai jogar? '))
while tot <= quant: #Quantidade de jogos
    cont = 0
    while True:  #Conferindo se o jogo vem com 6 unidades e sem repetiçao
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print ('-=' * 3 ,f'Sorteando {quant} jogos','-=' * 3)
for i, l in enumerate(jogos): #Resultado
    print(f'Jogo {i + 1}° : {l}')
    sleep(1)
print('Boa sorte camarada!')
