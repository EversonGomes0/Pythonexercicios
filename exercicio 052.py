tot=0
num=int(input('Digite um numero: '))
for c in range (1,num+1):
    if num % c == 0:
        print('\033[34m', end='')
        tot+=1
    else:
        print('\033[31m', end='')

    print(f'{c}',end=' ')
print(f'\n\033[mO número {num} foi divisivel {tot} vezes')
if tot == 2:
 print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')
