from time import sleep
def contador(i,f,p):
    print(f'contagem de {i} ate {f} em {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont:<5}',end='', flush=True)
            sleep(0.5)
            cont += p
        print ('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont:<5}',end='',flush=True)
            sleep(0.5)
            cont -=p
        print ('Fim')
    print('-=' * 30)

#Programa principal
contador(1,10,1)
contador(10,0,2)
print('Agora é sua contagem')
init = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
if pas < 0:
    pas *= -1
if pas == 0:
    pas = 1
contador(init,fim,pas)