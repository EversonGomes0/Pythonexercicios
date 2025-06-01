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

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print('\033[32m',txt.center(42),'\033[m')
    print(linha())

def menu(lista):
    print('\033[35mMENU PRINCIPAL\033[m'.center(42))
    print(linha())
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc