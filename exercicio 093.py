dados = dict()
dados['jogador'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input(f'Quantas partidas o {dados["jogador"]} jogou? : '))
dados['gols'] = list()
for c in range(0, dados['partidas']):
    gol = int(input(f'Quantos gols na {c} partida?'))
    dados['gols'].append(gol)
    del gol
dados['total'] = sum(dados['gols'])
print('-='*30)
print(dados)
print('-='*30)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["jogador"]} jogou {dados["partidas"]} partidas.')
for k,v in  enumerate(dados['gols']):
    print(f' => Na partida {k}, fez {v} gols.')
print (f'O total de gols foi de {dados["total"]} gols.')
