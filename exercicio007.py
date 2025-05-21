nota_1=float(input('Qual foi a 1° nota do aluno? '))
nota_2=float(input('Qual foi a 2° nota do aluno '))
media=(nota_1+nota_2) /2
print (f'A média do aluno no 1° semestre foi {media:.2f}\n')

# Isso aqui é só um complemento
if media >= 7:
    print ('O aluno está aprovado para o próximo trimestre!')
elif 7 > media >= 5:
  print ('O aluno está de recuperação!(VAI ESTUDAR)')
else:
    print('É o fim do ano pra ti ')
#Fiz antes de aprender hehe