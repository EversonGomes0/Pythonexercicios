def ficha():
    nome = str(input('Nome do jogador: '))
    gols = str(input('Quantidade de gols: '))
    if nome.strip() == '':
        nome = 'Desconhecido'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    resultado = f'O jogador {nome} fez {gols} gols no campeonato.'
    return resultado
#Programa principal
print(ficha())
print(ficha())
print(ficha())