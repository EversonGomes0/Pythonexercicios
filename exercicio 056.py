velho = 0
menos = 0
media = 0
somaidade = 0
idoso = '1'
nome = '<NAME>'
total=int(input('São quantas pessoas? '))
for pessoa in range(1, total+1):
    print (f'-----{pessoa}° PESSOA-----')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).upper().strip()[0]
    somaidade += idade
    media = somaidade/ total
    if pessoa == 1 and sexo == 'M':
        idade = velho
        idoso = nome

    if idade > velho and sexo == 'M':
            velho = idade
            idoso = nome
    if sexo == 'F' and idade < 20:
        menos += 1
print (f'A média da idade do grupo é de {media} anos.')
print (f'A idade do homen mais velho é de {velho} anos e seu nome é {idoso}')
print(f'A quantidade de mulheres com menos de 20 anos são {menos}')
