print ('-=-' * 11)
print ('    VAMO JOGAR PAR OU IMPAR')
print ('-=-' * 11)
import random
ganhou = 0
perdeu = 0
rodadas = 0
parouimpar = '1'
while True:
    rodadas += 1
    if rodadas > 5:
        break
    n = int(input('Diga um valor: '))
    jogada = str(input('Par ou impar? [P/I] ')).upper()[0]
    print('=-=' * 10)
    computador = random.randint(1,10)
    total = n + computador
    if total % 2 == 0:
      parouimpar = 'PAR'
    else:
        parouimpar = 'IMPAR'
    print(f'Você jogou {n} e o computador {computador} e o total foi {total} DEU {parouimpar}')
    if total % 2 == 0 and jogada == 'P' or total % 2 != 0 and jogada == 'I':
        print ('Você Venceu!\nVamos jogar novamente...')
        print ('=-=' * 10)
        ganhou += 1
    else:
        print ('VOCÊ PERDEU!')
        print ('=-=' * 10)
        perdeu += 1
print (f'GAME OVER!, você venceu {ganhou} vezes e perdeu {perdeu} vezes')
print ('=-=' * 10)
if ganhou > perdeu:
    print ('JOGADOR VENCEU!')
elif ganhou < perdeu:
    print ('COMPUTADOR VENCEU!')
print('=-=' * 10)
