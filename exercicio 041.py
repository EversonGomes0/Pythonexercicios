from datetime import date
print('=-=' * 10)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
ano = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
print (f'O atleta tem {idade} anos.')
if idade <= 9:
    print ('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print ('Classificação: SENIOR')
elif idade > 25:
    print ('Classificação: MASTER')
print('=-=' * 10)

