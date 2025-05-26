# Aprimoramento do exe 093
dados = dict()
jogadores = list()
gol = list()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gol.clear()
    for c in range(0, dados['partidas']):
        gol.append(int(input(f'Quantos gols na {c+1} partida? ')))
    dados['gols'] = gol[:]
    dados['total'] = sum(dados['gols'])
    jogadores.append(dados.copy())
    while True:
        resp = input('Quer continuar? [S/N]').strip().upper()[0]
        if resp in'SN':
            break
        print ('ERRO, RESPONDA APENAS S OU N ')
    if resp == 'N':
        break
print('-=' * 40)
print('cod', end=' ')
for i in dados.keys():
    print(f'{i:<15}',end='')
print()
print('-' * 40)
for pos, j in enumerate(jogadores):
    print(f'{pos:>3} ',end='')
    for d in j.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca > len(jogadores):
        print (f'ERRO! não existe jogador com esse codigo!')
    else:
        print (f'--- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<<<VOLTE SEMPRE>>>')