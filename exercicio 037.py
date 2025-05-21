num=int(input('Digite um número inteiro:'))
binario=bin(num)[2:]
octal=oct(num)[2:]
hexadecimal=hex(num)[2:]
escolha=str(input('''Digite [1] para binário
Digite [2] para octal 
Digite [3] para hexadecimal
Sua opção: '''))
if escolha =='1':
    print(f'O número em binário é {binario}')
elif escolha == '2':
    print (f'O número em octal é {octal}')
elif escolha == '3':
    print (f'O número em hexadecimal é {hexadecimal}')
else:
    print ('Número inválido')
