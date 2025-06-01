from utilidadescev import moeda
from moeda import *

#\Treinando modulos
num = float(input('Digite o preço: '))
print (f'A metade de {moeda(num,True)} é {moeda(metade(num))}')
print (f'O dobro de {moeda(num)} é {moeda(dobro(num))}')
print (f'O aumento é {moeda(aumentar(num,10))}')
print(f'A diminuição é {moeda(diminuir(num,13))}')

