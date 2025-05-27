from time import sleep
def maior(* valores):
    print('-=' * 30)
    tam = len(valores)
    print('Analisando os valores passados...')
    for v in valores:
        print(v, end=' ')
        sleep(0.3)
    print (f'Foram informados {tam} valores ao todo')
    print (f'O maior valor foi {max(valores)}')

#Programa principal
maior(2,8,5,3,6)
maior(0,5,1,6,9)
maior(34,56,7,8,9,434,2,334,56)
maior(4)
maior(8,3)
maior(0)