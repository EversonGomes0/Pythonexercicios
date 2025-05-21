from datetime import date
anonasc=int(input('Digite seu ano de nascimento: '))
anoatual=date.today().year
idade= anoatual - anonasc
print(f'Você tem {idade} anos ')
if idade < 18:
    print(f'Vai faltar {18 - idade} anos para se alistar.')
    print(f'Seu alistamento será em {anonasc + 18}')
elif idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE.')
elif idade > 18:
    print(f'Você deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {anonasc + 18}')
