casa=float(input('Qual o valor da casa? R$'))
salario=float(input('Qual o valor do seu salario? R$'))
anos=int(input('Quantos anos você quer pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 0.30
print (f'Para pagar uma casa de R${casa:.2f} em {anos} anos, ',end= '')
print (f'A prestação será de R${prestacao:.2f} por mês ')
if prestacao <= minimo:
    print('Empréstimo \033[1;34mAPROVADO!\033[M')
else:
    print('Empréstimo \033[1;31mREPROVADO!\033[m')
