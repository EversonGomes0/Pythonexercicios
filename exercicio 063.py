print ('=' * 15)
print ('Sequencia de Fibonacci')
termo =int(input('Quantos termos são? '))
n1 = 0
n2 = 1
cont = 1
print (f'{n1} -> {n2}', end=' -> ')
while cont <= termo:
 proximo = n1 + n2
 print(proximo, end=' -> ')
 n1 = n2
 n2 = proximo
 cont += 1
print('FIM')
