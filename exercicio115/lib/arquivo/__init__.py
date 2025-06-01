from exercicio115.lib.interface import *
def arquivoexiste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for lin in a:
            dado = lin.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos.')

def cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro a abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de digitar ')
        else:
            print(f'{nome} cadastrado com sucesso')
