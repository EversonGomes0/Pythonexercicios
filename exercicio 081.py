lista = list()
# Criando uma lista infinita
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
        #quebrando o looping
print ('-' * 30)
lista.sort(reverse=True)
#complementando algumas informações
print (f'Você digitou {len(lista)} elementos')
print (f'Os valores em ordem decrescente {lista}')
if 5 in lista:
    print ('O valor 5 faz parte da lista')
else:
    print ('O valor 5 não faz parte da lista')