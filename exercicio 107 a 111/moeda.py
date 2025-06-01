#Exercicio 107

def aumentar(n,taxa=0):
    res = n + (n * taxa / 100)
    return res

def diminuir(n,taxa=0):
    res = n - (n * taxa / 100)
    return res

def dobro(n):
    res = n * 2
    return res

def metade(n):
    res = n / 2
    return res

def moeda(n=0,real='R$'):
    return f'{real}{n:>2.2f}'.replace('.',',')

def resumo(n=0,aum=0,dim=0):
    print ('-' * 30)
    print ('RESUMO DO VALOR'.center(30))
    print ('-' * 30)
    print(f'Preço analisado: \t{moeda(n):>10}')
    print(f'Dobro do preço: \t{moeda(dobro(n)):>10}')
    print(f'Metade do preço: \t{moeda(metade(n)):>10}')
    print(f'{aum}% de aumento: \t{moeda(aumentar(n,aum)):>10}')
    print(f'{dim}% de redução: \t{moeda(diminuir(n,dim)):>10}')
    print('-' * 30)
