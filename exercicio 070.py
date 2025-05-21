print('=' * 15)
print('LOJAS GOMES DO CABRITAO')
print('=' * 15)
barato = 0
soma = totmil = cont = menor_valor = 0
produto_barato = ''
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Qual o preço ? R$'))
    soma += valor
    cont += 1
    if valor > 1000:
        totmil += 1
    if cont == 1:
        menor_valor = valor
        produto_barato = produto
    else:
        if valor < menor_valor:
            menor_valor= valor
            produto_barato = produto
    r = str(input('Quer continuar? [S/N]: ')).upper()
    if r == 'N':
        break
print ('=' * 25)
print ('     FIM DO PROGRAMA ')
print (f'O Total gasto na compra foi de R${soma:.2f}')
print (f'Os produtos mais caros acima de 1000R$ foram {totmil} produtos')
print (f'O produto mais barato foi {produto_barato} que custa R${menor_valor:.2f} ')