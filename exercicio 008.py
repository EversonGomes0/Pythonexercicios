medida_da_casa=int(input('Qual a medida em metros da casa? M'))
metros=medida_da_casa
centimetros= metros * 100
milimetros = centimetros*10    # O comando \n eu posso usar pra evitar de usar tanto o print
print ('A casa medida em metros é {}M'.format(metros))
print ('A casa medida por centímetros fica {}CM'.format(metros*100))
print ('A casa medida por milímetros fica {}ML\n'.format(metros*1000))

#Extra que eu fiz
quilometros = metros /1000
print ('A casa em quilômetros é {}KM'.format(quilometros))