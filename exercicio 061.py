print ('-=-' * 15)
print ('TERMOS DA PA')
print ('-=-' * 15)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = pri
cont = 1
while cont <= 10:
    print(termo, end=' -> ')
    termo += razao
    cont += 1
