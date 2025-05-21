preco=(float(input('Qual o preço do produto? R$')))
desconto=float(input('Qual a porcentagem do desconto? %'))
novo_preco=preco*(desconto/100)
preco_desconto=preco-novo_preco
print ('O novo valor com desconto foi de R${:.2f}'.format(preco-novo_preco))
