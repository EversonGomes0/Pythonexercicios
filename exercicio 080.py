lista = []
 #Organizando uma lista sem usar sorted()
for c in range(0,5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        # caso o número seja menor que o ultimo da lista
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'adicionado na posição {pos} da lista')
                break
            pos += 1
print (f'Os valores digitados em ordem foram: {lista} ')