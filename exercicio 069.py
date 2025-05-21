maior = 0
homen = 0
mulheres = 0
while True:
    print('=' * 15)
    print('CADASTRE UMA PESSOA')
    print('=' * 15)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = str(input('Sexo: [F/M]: ')).upper()
    if sexo == 'M':
        homen += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    print('=' * 15)
    r = str(input('Quer continuar? [S/N]: ')).upper()
    if r == 'N':
        break
print (f'Existem {maior} pessoas maiores de idade')
print (f'Foram cadastradas {homen} Homens ')
print (f'Foram cadastradas {mulheres} mulheres menores de 20 anos')