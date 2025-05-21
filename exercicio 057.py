sexo = str(input('Informe seu sexo: [M/F]: ')).upper().strip()[0]
while not sexo in 'MmF':
    sexo = str(input('ERRO!! Tente novamente: [M/F]: ')).upper().strip()[0]
if sexo == 'M':
    print ('Sexo Masculino')
elif sexo == 'F':
    print ('Sexo Feminino')
