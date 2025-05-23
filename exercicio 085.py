# fazendo uma lista e separando as por Par e Impar
numeros = [[],[]]
for c in range(0,7):
    num = int(input(f'Digite o {c+1}° valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros.sort()
numeros[0].sort()
numeros[1].sort()
print ('-=-' * 30)
print(f'Os valores foram : {numeros}')
print (f'Os valores pares: {numeros[1]}')
print(f'Os valores impares: {numeros[0]}')