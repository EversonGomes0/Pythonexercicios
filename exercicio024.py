city=str(input('Digite o nome da cidade: ')).strip().upper()
first=str(input('O primeiro nome dela começa: ')).split()[0].upper()
if city.startswith(first):
    print(True)
else:
    print(False)
#print(city[:5] == 'Santo')
#print (first)
#print(city.startswith('Santo'))
