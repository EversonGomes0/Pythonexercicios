def fact(n,show=False):
    """
    >- Formação de uma fatorial
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar o calculo de fatorial
    :return: retorna a fatorial de n
    """
    resultado = 1
    c = 0
    for i in range(1,n+1):
        c += 1
        if show:
        #Formatando os sinais de multiplicação e o de igual
            print(i, end=' ')
            if c < n:
                print('x',end=' ')
            else:
                print('=',end=' ')
        resultado *= i
    return resultado
#Programa Principal
print(fact(6,True))