# Criando a lista
lista = list()
while True:  #começando o looping
    valor = int(input('Digite um valor: '))
    #criando uma lista sem ter valores duplicados
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado!, não vou adicionar...')
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-' * 30)
print(f'Você digitou os valores ')
# lista em ordem crescente
lista_ordenada = sorted(lista)
for v in lista_ordenada:
    print(f'{v} ', end='')
    