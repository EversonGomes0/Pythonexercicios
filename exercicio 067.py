while True:
    print('-=' * 30)
    n = int(input('Quer ver a tabuáda de qual valor? '))
    if n < 0:
        print('Programa finalizado com sucesso, Volte sempre!')
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
