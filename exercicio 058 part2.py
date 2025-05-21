import random
tentativas = 0
computador = random.randint(0, 10)

print('Sou o computador, estou pensando em um número entre 0 e 10...')

# Valida o primeiro palpite:
while True:
    try:
        palpite = int(input('Consegue adivinhar qual é?\n Qual o seu palpite? '))
        break
    except ValueError:
        print('Entrada inválida! Digite apenas números inteiros.')

while palpite != computador:
    if palpite > computador:
        print('Menos... tente novamente.')
    elif palpite < computador:
        print('Mais... tente novamente.')

    tentativas += 1

    # Valida os próximos palpites:
    while True:
        try:
            palpite = int(input('Novo palpite: '))
            break
        except ValueError:
            print('Entrada inválida! Digite apenas números inteiros.')
