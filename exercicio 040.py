nota1=float(input('Qual a primeira nota: '))
nota2=float(input('Qual a segunda nota: '))
media = (nota1 + nota2) / 2
print (f'Sua média foi {media:.2f}')
if media >= 7:
    print('Parabéns!, você foi aprovado.')
elif 5 <= media < 7:
    print('Eita!, você está de recuperação.')
elif media < 5:
    print('Deu ruim! você foi reprovado.')
