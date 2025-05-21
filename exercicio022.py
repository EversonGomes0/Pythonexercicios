name = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculo é {name.upper()}')
print(f'Seu nome em minúscuslo é {name.lower()}')
print(f'Seu nome sem espaço tem {(len(name)+1)-name.count(" ")} letras')
print(f'Seu primeiro nome é {name.split()[0]} e ele tem {name.find(' ')} letras')
                                         #Outra maneira {len(name.split)[0]}
