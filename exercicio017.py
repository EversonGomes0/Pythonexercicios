from math import hypot,pow,sqrt,ceil
co=float(input('Qual o lado do cateto oposto? '))
ca=float(input('Qual o lado do cateto adjacente? '))
#hipot=hypot(co,ca)
print (f'A hipotenusa do trinâgulo vale {ceil(hypot(co,ca))}')
# Modo casual
hipot=sqrt(pow(co,2)+pow(ca,2))
print (f'Usando o método tradicional também deu {ceil(hipot)}')