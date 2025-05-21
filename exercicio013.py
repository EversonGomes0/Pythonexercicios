salario=float(input('Qual o sálario do funcionário? R$'))
aumento=float(input('Qual o aumento em porcentagem? %'))
novo=salario + (salario*aumento/100)
print ('O novo sálario do funcinário é de R${}'.format(novo))
