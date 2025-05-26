dados = list()
cadastro = dict()
soma = 0
mulheres = list()
while True:
    #Cadastrando uma pessoa em dicionário e depois jogando as em uma lista
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
    while cadastro['sexo'] not in 'FM':
        print ('ERRO, por favor digite apenas M ou F.')
        cadastro['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
    cadastro['idade'] = int(input('Idade: '))
    dados.append(cadastro.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for c in range(0, len(dados)):
    #Somando as idades
     if dados[c]['sexo'] == 'F':
         mulheres.append(dados[c]['nome'])
         # colocando as mulheres em uma lista
     soma = dados[c]['idade']
media = soma / len(dados)
# fazendo a média das idades
print ('-=' * 30)
# Resultado final
print (f'A) No total {len(dados)} pessoas foram cadastrados.')  #Total de pessoas cadastradas na lista
print(f'B) A média das idades foi de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for i,m in enumerate(mulheres):
    print (f'{mulheres[i]}, ')
print ('D) Lista das pessoas que estão acima da média: ')
for p in dados:
    if  p['idade'] >= media:
        print ('  ')
        for k,v in p.items():
            print (f' {k} = {v} ;', end='')
        print()
print('<<<ENCERRADO>>>')
