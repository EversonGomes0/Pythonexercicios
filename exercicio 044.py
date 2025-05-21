print('----------Lojas linho----------')
valor=float(input('Qual o valor das compras? R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
escolha=int(input('Qual a opção?\n'))
if escolha == 1:
    print(f'Sua compra de R${valor} vai custar R${valor*0.9}  ')
elif escolha == 2:
    print(f'Sua compra de R${valor} vai custar R${valor*0.95} no cartão')
elif escolha == 3:
    print(f'Sua compra será parcelada em 2x de {valor/2} SEM JUROS')
elif escolha == 4:
    parcelas=int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${(valor + (valor*0.2))/parcelas:.2f} COM JUROS')
    print(f'Sua compra de R${valor} vai custar R${valor+(valor*0.2)}')
