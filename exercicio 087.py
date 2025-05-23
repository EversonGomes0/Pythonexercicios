matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Criando uma matriz
soma = mai = men = pares =  0
for l in range(0, 3):
   for c in range(0,3):
       valor = int(input(f'Digite um valor para [{l+1},{c+1}]: '))
       if valor % 2 == 0:
           pares += valor
       matriz[l][c] = valor
print ('-=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()
print(f'A soma dos valores pares:{pares}')  # Fazendo a soma dos pares
for l in range(0,3):
    soma += matriz[l][2]
print(f'A soma dos valores da 3° coluna é {soma}') #Fazendo a soma da 3° coluna
for c in range(0,3):
    if c == 0 or matriz[1][c] > mai :
        mai = matriz[1][c]
print(f'O maior valor da 2° linha é {mai}') # Verificando quem é  maior da 2° linha
