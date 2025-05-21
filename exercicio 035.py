print ('=-='*10)
print('Analisador de triângulo')
print('=-='*10)
a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if a < b+c and b < c+a and c < a + b:
    print('\033[1;32mÉ Possivel formar um triângulo')
else: print('\033[31mNão é possível formar um triângulo')