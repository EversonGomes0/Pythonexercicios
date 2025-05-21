velocidade=int(input('Qual a velocidade atual do carro: Km/h'))
if velocidade > 80:
    multa=(velocidade - 80) * 7
    print(f'MULTADO!, Você excedeu o limite que é de 80km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}')
else:
    print('Ok, velocidade normal. Tenha um bom dia!')