def leiadinheiro(msg):
    while True:
        msg = input(msg)
        if ',' in msg:
            msg = msg.split(',')
        if msg.isnumeric():
           return int(msg)
        else:
            print (f'\033[m31 Erro, {msg} é inválido\033[m')
