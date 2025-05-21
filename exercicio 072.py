numeros = ('Zero','Um','Dois','Tres','Quatro','Cinco',
           'Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quartoze','Quinze',
           'Dezesseis','Dezesete','Dezoito','Dezenove','Vinte')
while True:
 num = int(input('Digite um número de 0 a 20: '))
 if len(numeros) <= 21:
  break
 print('Tente novamente.')
print (f'Você digitou o número {numeros[num]}.')
