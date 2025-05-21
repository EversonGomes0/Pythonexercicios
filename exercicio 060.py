n = int(input('Digite um número inteiro: '))
c = n
f =1
while True:
    print (f'{c}',end=' ')
    print (f'X ' if c > 1 else '= ',end='' )
    f *= c
    c -= 1
    if c == 0:
        break

print (f)
#print (f'O fatorial de {num} é {fatorial}')
