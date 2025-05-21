nome=input('digite seu nome: ')
print("Boas vindas!, {}".format(nome))
valor=int(input('Valor do PC: R$'))
taxa=float(input('Taxa: %'))
t=valor*taxa/100
nv=t+valor
print('O novo valor sobre o Pc foi: R${}'.format(nv))

