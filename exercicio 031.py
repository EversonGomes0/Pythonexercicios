viagem=float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {viagem}KM ')
preco=viagem * 0.50 if viagem <= 200 else viagem * 0.45
print (f'O preço da passagem vai ser \033[34mR${preco:.2f}')