from exercicio115.lib.interface import *
from exercicio115.lib.arquivo import *
from time import sleep
arq = 'gomes.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        #opção de lista o conteúdo do arquivo
        lerarquivo(arq)
    elif resposta == 2:
        #opção de cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        sleep (1)
        cabeçalho('Saindo do programa, Volte sempre')
        break
    else:
        print('\033[31mERRO, RESPOSTA INVALIDA\033[m')
    sleep (1)