print ('-=-' * 15)
print ('TERMOS DE PA')
print('-=-' * 15)
pri = int(input('Primeiro termo: '))
razao = int(input('Qual a razão: '))
termo: int = pri
cont = 1
mais = 10
total = 0
while mais != 0:
 total += mais
 while cont <= total:
    print(termo, end=' -> ')
    termo += razao
    cont += 1
 print('PAUSA')
 mais = int (input('Quantos termos quer adicionar? '))
print ('FIM')
print (f'O total de termos foi de  {total}')
