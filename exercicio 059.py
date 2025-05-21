opcao = 0
a = (int(input('Digite um valor:   ')))
b = (int(input('Digite o segundo valor:  ')))
while opcao != 5:
    print('=' * 15)
    opcao = int(input('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair \n>>>>>Qual a sua opção? '))
    while not opcao in (1,2,3,4,5,):
        opcao = int(input('Resposta inválida, tente novamente: '))
    if opcao == 1:
        print (f'A soma entre {a} e {b} é {a + b }')
    elif opcao == 2:
        print (f'A multiplicação entre {a} e {b} é {a * b}')
    elif opcao == 3:
        print(f'Entre {a} e {b} o maior é {max(a, b)}')
    elif opcao == 4:
        print('informe novamente')
        a = (int(input('Digite um valor: ')))
        b = (int(input('Digite o segundo valor: ')))
    elif opcao == 5:
        print('Finalizando...')
        from time import sleep
        sleep(2)
    else :
        print ('Opcao invalida!')
