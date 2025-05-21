dinheiro=float(input('Olá! quanto o senhor(a) tem em sua carteira? R$'))
em_dolar =dinheiro//5.81
print ('Você pode comprar {} US$'.format(em_dolar))
  #Testando o comando if,elif e else
if em_dolar*8 > 120:
    salariominimo=em_dolar*8
    print (' Você vai literalmente receber um salário minimo de {} trabalhas em 8 horas em boston '.format(salariominimo))
else :
    print('Boa sorte nos EUA')
    # Fiz o calculo meio errado mas consegui usar a condicional