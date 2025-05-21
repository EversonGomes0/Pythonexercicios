print ('=' * 15)
print ('LISTAGEM DE PREÇOS')
print ('=' * 15)
produtos = ('Lápis',
            'Borracha',
            'Caderno',
            'Estojo',
            'Transferidor',
            'Compasso',
            'Mochila',
            'Caneta',
            'Livro',)
preco = (1.75,
         2.00,
         15.90,
         25.00,
         4.20,
         9.99,
         120.32,
         22.30,
         34.90,)
for c in range(0,len(produtos)):
      print (f'{produtos[c]}.........R${preco[c]}')