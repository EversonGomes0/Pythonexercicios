def leiaint(msg):
    while True:
        try:
            msg = int(input(msg))
        except (ValueError, TypeError):
            print('Dado informado invalido')
        except (KeyboardInterrupt, EOFError):
            print('Entrada de dados interrompida')
        else:
            return msg

def leiafloat(msg):
    while True:
        try:
            msg = float(input(msg))
        except (ValueError, TypeError):
            print('Dado informado invalido')
        except (KeyboardInterrupt, EOFError):
            print('Entrada de dados interrompida')
        else:
            return msg

#Programa Principal
n = leiaint('Digite um número inteiro: ')
print(f'Você digitou {n}')
f = leiafloat('Digite um número real: ')
print(f'Você digitou {f}')
