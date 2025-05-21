num = (int(input('Digite um numero: ')),
      int(input('Digite outro numero: ')),
      int(input('Digite mais um numero: ')),
      int(input('Digite o ultimo numero: ')))
if 9 in num:
   print (f'O número 9 apareceu {num.count(9)} vezes')
else:
    print('O número 9 não foi digitado')
if 3 in num:
  print(f'O numero 3 está na posição {num.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n,end= ' ')