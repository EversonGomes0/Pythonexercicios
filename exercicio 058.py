import random
tentativas = 0
computador = random.randint(0,10)
print('Sou o computador, estou pensando em um numero entre 0 e 10...')
palpite = int(input('Consegue adivinhar qual é?\n Qual o seu palpite? '))
while palpite != computador:
    if palpite > computador:
        palpite = int(input('Menos... tente novamente: '))
        tentativas += 1
    elif palpite < computador:
        palpite = int(input('Mais... tente novamente: '))
        tentativas += 1
if tentativas > 0 < 4 :
    print(f'Você acertou com {tentativas} tentativas. Parabéns!!')
elif tentativas == 0:
    print('Parabéns! acertou de primeira')
else:
    print(f'Demorou demais! foram {tentativas} tentativas para acertar')
