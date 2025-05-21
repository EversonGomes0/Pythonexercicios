import random,time
itens=('Pedra','Papel','Tesoura')
print('-=-' * 10)
print('COMPUTADOR VS JOGADOR')
print('''Suas opçôes:
 [0] Pedra
 [1] Papel
 [2] Tesoura''')
pedra='1'
papel='2'
tesoura='3'
jogador=int(input('Qual a sua jogada? '))
computador=random.randint(0,2)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!')
time.sleep(1)
print('-='*10)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*10)
if jogador == 0 and computador == 1:
    print('COMPUTADOR GANHOU!')
elif jogador == 1 and computador == 0:
    print('JOGADOR GANHOU!')
elif jogador == 2 and computador == 0:
    print('COMPUTADOR GANHOU!')
elif jogador == 0 and computador == 2:
    print('JOGADOR GANHOU!')
elif jogador == 1 and computador == 2:
    print('COMPUTADOR GANHOU!')
elif jogador == 2 and computador == 1:
    print('JOGADOR GANHOU!')
elif jogador == computador:
    print('EMPATE!')
print('-='*10)