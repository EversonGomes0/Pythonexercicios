from time import sleep
  #1° Exercicio
a = int(input())
b = int(input())
print (f'A soma é {a + b}')
 #2 exe
a = int(input('Digite um número qualquer:'))
if a % 2 ==0:
    print ('É PAR')
else:
    print ('É IMPAR')
sleep(2)
 #3 exe
for c in range(1,11):
    print (c,end=' ')
sleep(2)
 #4 exe
a = int(input('Digite um número para a tabuada: '))
for c in range(1,11):
    print (f'{a} X {c} = {a*c}')
sleep(2)
 #5 exe
palavra = str(input('Digite uma palavra: ')).lower()
c = 0
for letra in palavra:
    if letra in 'aeiou':
        c += 1
print (f'Existem {c} vogais ')
 # 6 exe
numeros = []
for i in range(1,6):
    numero = int(input(f'Digite o {i}° numero: '))
    numeros.append(numero)
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print (numeros)
print (pares)
 # 7 exercicio

