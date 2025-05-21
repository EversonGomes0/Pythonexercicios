salario=float(input('Qual o sálario do funcionário? R$'))
aumento = salario +(salario*0.10) if salario > 1250 else salario +(salario*0.15)
print (f'O  Novo sálario foi de  R$\033[1;32m{aumento}')