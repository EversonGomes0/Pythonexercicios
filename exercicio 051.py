print('=' * 15)
print(' 10 TERMOS DE UMA PA')
print('=' * 15)
pri=int(input('Primeiro termo: '))
razao=int(input('Qual a razão: '))
decimo=pri+(10-1)*razao
for c in range(pri,decimo+razao,razao):
    print(c,end= '-> ')
print('ACABOU')