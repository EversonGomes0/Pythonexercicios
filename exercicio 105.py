def notas(*n, sit=False):
    """
    -> Boletim de notas
    :param n: Notas parciais
    :param sit: (opcional) Mostra a situacao do aluno)
    :return: Dicionario com as notas e a situacao
    """
    nota = dict()
    nota['total'] = len(n)
    nota['Maior'] = max(n)
    nota['Menor'] = min(n)
    nota['Média'] = sum(n)/len(n)
    if sit:
        if nota['Média'] >= 7:
            nota['situação'] = 'Boa'
        elif nota['Média'] >= 5:
            nota['situação'] = 'Razoável'
        else:
            nota['situação'] = 'Ruim'
    return nota
#Programa Principal
resp = notas(6,7,4,8, sit = True)
print(resp)