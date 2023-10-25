name = str(input('Digite o seu nome completo: ')).strip()
silva = name.lower().find('silva')
if silva == -1:
    print('O nome {} não possui o sobrenome Silva.'.format(name))
else:
    print('O nome {} possui o sobrenome Silva.'.format(name))
