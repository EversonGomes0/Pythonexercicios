print ('-=-' * 10)
num1=int(input('Primeiro número: '))
num2=int(input('Segundo número: '))
print ('-=-' * 10)
print (f'''Tente adivinhar!
 [1] O número {num1} é maior que o {num2}
 [2] O número {num2} é maior que o {num1}
 [3] Os dois números são iguais''')
print('-=-' * 10)
escolha=str(input('Sua escolha: '))
if num1 > num2 :
   correto = '1'
elif num2 > num1 :
    correto = '2'
elif num1 == num2:
    correto = '3'
if  correto == escolha:
    print('\033[1;34mParabéns!! Você acertou!\033[m')
else:
    print('\033[1;31mPoxa! você errou! ou resposta inválida\033[m')
    print(f'A opção correta era {correto}')