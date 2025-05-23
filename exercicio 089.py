alunos = list()
lista = list()
while True:  # Boletim de alunos com suas notas e médias
    nome = str(input('Nome:'))
    lista.append(nome)
    nota1 = float(input('Nota 1: '))
    lista.append(nota1)
    nota2 = float(input('Nota 2: '))
    lista.append(nota2)
    media = (nota1 + nota2) / 2
    lista.append(media)
    alunos.append(lista[:])
    lista.clear()
    resp = str(input('Terminou? S/N')).strip().upper()[0]
    if resp == 'S':
        break
print ('-=-' * 30) #Lista dos alunos e suas médias
print('ALUNOS           MÉDIA')
for c in range(0,len(alunos)):
    print(f'{c} {alunos[c][0]:<15}   {alunos[c][3]}')
while True:
    nota_aluno = int(input('Mostrar notas de qual aluno? (999 para parar) ')) #Analisando notas pela contagem
    print(f'As notas de {alunos[nota_aluno][0]} são {alunos[nota_aluno][1],alunos[nota_aluno][2]} ')
    if nota_aluno == 999:
        break