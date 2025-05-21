num=int(input('Digite um numero: '))
print('Analisando...')
import time
time.sleep(3)
if num % 2 == 0:
    print(f'O número \033[1;38m{num} é PAR!')
else:
    print(f'O número \033[1;31m{num} é ÍMPAR!')