expressao = str(input('Digite a expressao: ')) # Verificando se expressão esá correta
pilha = []
for simb in expressao: # Analisando cada simbolo
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print ('Sua expressão está válida!')
else:
    print('Sua expressão não está válida!')