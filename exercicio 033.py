a=int(input('Primeiro valor: '))
b=int(input('Segundo valor: '))
c=int(input('Terceiro valor:'))
#Verificando o menor
menor = a
if b < a and b < c: menor = b
elif c < a and c < b: menor = c
#Verificando o maior 
maior = b
if a > c and a > b: maior = a
elif c > b and c > a: maior = c
print (f'''Menor valor: \033[34m{menor}\033[m 
Maior valor: \033[35m{maior} ''')