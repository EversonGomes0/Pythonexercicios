def leiaint(msg):
    while True:
        msg = str(input(msg))
        if msg.isnumeric():
            return int(msg)
        else:
            print ('\033[31mERRO, digite um número inteiro válido\033[m')
#Programa principal
n = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {n}')