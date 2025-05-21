import random
numero=random.randint(0,5)
print('-=-'*10)
print('Estou pensando em um numero entre 0 e 5')
print('Consegue adivinhar qual foi o numero escolhido?')
print('-=-'*10)
escolha=int(input())
if escolha == numero:
    print(f'Parabéns !! Você acertou! é o {numero}')
else:
    print(f'Você errou! Eu pensei no numero {numero} e não no {escolha}' )