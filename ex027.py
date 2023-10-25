name = str(input('Digite o seu nome completo: ')).strip()
name_split = name.split(' ')
print('=====')
print('O seu primeiro nome é {}.'.format(name_split[0]))
print('O seu último nome é {}.'.format(name_split[-1]))
print('=====')

#.format(nome[len(nome)-1])
