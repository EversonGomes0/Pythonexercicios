cadastro = []
lista = []
mai = men = soma = 0
while True:   #Cadastrando as pessoas
    nome = str(input('Nome: '))
    lista.append(nome)
    peso = float(input('Peso: '))
    lista.append(peso)
    if len(cadastro) == 0: #Lendo quem é o maior e menor peso
        mai = men = lista[1]
    else:
        if lista[1] > mai:
            mai = lista[1]
        elif lista[1] < men:
            men = lista[1]
    soma += peso #Somando os pesos
    cadastro.append(lista[:])
    lista.clear()
    resp = input('Quer continuar? [S/N]').upper()[0].strip()
    if resp in 'Nn':
        break
media = soma / len(cadastro) #Fazendo a média dos pesos
print (f'O total de pessoas cadastradas foi {len(cadastro)} pessoas.')  #Total de pessoas registradas
print (f'O maior peso foi {mai}KG dos nome :', end='') #Quem teve o maior peso
for p in cadastro:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print (f'\nE o menor peso foi {men}Kg dos nome :', end='') #Quem teve o menor peso
for p in cadastro:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print (f'\nA média dos pesos foi de {media:.2f}KG') #Quem está acima e abaixo da média das pessoas
print ('Os que estão acima da média: ',end='')
for p in cadastro:
    if p[1] > media:
        print(f'[{p[0]}]',end= '')
print('\nOs que estão abaixo da média: ',end='')
for p in cadastro:
    if p[1] < media :
        print(f'[{p[0]}]',end='')