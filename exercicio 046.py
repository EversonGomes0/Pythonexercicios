from time import sleep
print('CONTAGEM REGRESSIVA')
for c in range(10, 0, -1 ):
    print('\033[1;31m', end='')
    print(c)
    sleep(1)

print('\033[1;34mFELIZ ANO NOVO!!')
