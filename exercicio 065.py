resp ='1'
soma = 0
cont = 0
maior = 0
menor = 0
while True:
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior :
            maior = n
        elif n < menor :
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp in 'Nn':
        break
media = soma / cont
print(f'A média dos {cont} números é de {media :.2f}')
print (f'O maior número foi {maior} e o menor foi {menor} ')