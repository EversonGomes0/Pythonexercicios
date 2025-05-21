num= str(input('Informe um número: '))
print('\033[34mAnalisando...\033[m')
#u= num //1 % 10
#d= num//10 % 10
#c= num//100 % 10
#m= num//1000 % 10
#print(f'Unidade: {u}')
#print(f'Dezena: {d}')
#print(f'Centena: {c}')
#print(f'Milhar: {m}')
if len(num) == 1:
  print (num[0])
elif len(num) == 2:
   print (num[0])
   print (num[1])
elif len(num) == 3:
    print(num[0])
    print(num[1])
    print(num[2])
elif len(num) == 4:
    print(num[0])
    print(num[1])
    print(num[2])
    print(num[3])
else:
    print('Número inválido')
