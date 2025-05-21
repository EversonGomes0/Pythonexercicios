from datetime import date
maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input(f'Qual a data de nascimento da {c}° pessoa?\n' ))
    atual = date.today().year
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1
print(f'No total {maior} pessoas antigiram a maioridade e {menor} ainda não antigiram.')
