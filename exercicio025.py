name=str(input('Qual o seu nome completo? ')).title().strip()
sobrenome=str(input('Você deseja escolher qual sobrenome?')).title().strip()
if sobrenome in name:
   print(f'Tem \033[36m{sobrenome}\033[m no seu nome? \033[36m{sobrenome in name}')
else:
   print(f'Tem \033[1;31m{sobrenome}\033[m no seu nome? \033[1;31m{sobrenome in name}')


