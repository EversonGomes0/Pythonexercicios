aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'RECUPERAÇÃO'
elif aluno['media'] < 5:
    aluno['situacao'] = 'REPROVADO'
print ('=' * 30)
for k,v in aluno.items():
    print(f'- {k} é igual a {v}')
