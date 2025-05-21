a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if a < b+c and b < c+a and c < a+b:
 print('É possivel formar um trinângulo ',end='')
 if a==b and c==a and b==c:
   print('Equilátero')
 elif a!=b and a!=c and b!=c:
   print('Escaleno')
 elif a==b or a==c or b==c:
  print('Isóceles')
else:
  print('Não é possivel formar um trinagulo')
  