nome = input('Digite o nome de uma cidade: ')
santo = nome.find('Santo')
print(santo)
if santo == -1:
    print('A cidade {} não possui Santo no nome.'.format(nome))
else:
    print('A cidade {} possui Santo no nome.'.format(nome))
