peso=float(input('Qual é o seu peso? KG'))
altura=float(input('Qual é a sua altura? M'))
imc=peso / (altura ** 2 )
print (f'Seu IMC é de {imc:.2f} ')
if imc < 18.5:
    print ('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está sobrepeso')
elif 30 <= imc < 40:
    print('Você está na obesidade')
elif imc >= 40:
    print('Você está com obeseidade mórbida')
