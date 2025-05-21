from datetime import date
ano=int(input('Digite um ano qualquer(digite 0 para o ano atual): '))
if ano == 0:
    ano = date.today().year
    print (ano)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[7;37mO ano {ano} é BISSEXTO!')
else:
    print(f'\033[32mO ano {ano} Não é BISSEXTO!')