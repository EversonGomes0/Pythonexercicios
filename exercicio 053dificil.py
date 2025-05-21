frase=str(input('Digite um frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):  #inverso junto[::-1]
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É um palindromo')
else:
    print('Não é um panlindromo')
