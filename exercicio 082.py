lista = list() # Separando listas em pares e impares
pares = list()
impares = list()
while True:
    valor = (int(input('Digite um valor: ')))
    lista.append(valor)    #Usando as condicionais
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A lista completa é {lista}')
print (f'Os pares da lista são {pares}')
print (f'Os impares da lista são {impares}')
