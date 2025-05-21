par = 0
impar = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
      par += n
    elif n % 2 == 1:
     impar += n
print(f'A soma dos valores pares foi {par}')
print(f'A soma dos valores impares foi {impar}')
