from datetime import date #Cadastrando um trabalhador
trabalhador = {}
ano_atual = date.today().year
trabalhador['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
trabalhador['ano de nascimento'] = ano_atual - nasc
trabalhador['ctps'] = int(input('Carteira de trabalho: (0 não tem) '))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratacao: '))
    trabalhador['salario'] = float(input('Salario: '))
    trabalhador['aposentadoria'] = trabalhador['contratacao'] + 35 - ano_atual
print('-='*30)
for k,v in trabalhador.items():
    print(f'- {k} tem o valor {v}')