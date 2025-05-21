menor = 0
maior = 0
for pessoa in range (1,6):
    peso=float(input(f'Qual o peso da {pessoa}° pessoa? '))
    if pessoa == 1:
         maior = peso
         menor = peso
    else:
          if peso > maior:
             maior = peso
          elif peso < menor:
             menor = peso
print(f'O maior peso foi {maior}Kg e o menor peso foi {menor}Kg.')
