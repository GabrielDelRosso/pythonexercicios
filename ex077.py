vogais = 'AEIOU'
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
print('=' * 30)
print('{:^30}'.format('VERIFICADOR DE VOGAIS'))
print('=' * 30)
for c in range(0, 12):
    print(f'Na palavra {palavras[c]} temos as vogais: ')
    if vogais[0] in palavras[c]:
        numa = palavras[c].count('A')
        print('A ' * numa)
    if vogais[1] in palavras[c]:
        nume = palavras[c].count('E')
        print('E ' * nume)
    if vogais[2] in palavras[c]:
        numi = palavras[c].count('I')
        print('I ' * numi)
    if vogais[3] in palavras[c]:
        numo = palavras[c].count('O')
        print('O ' * numo)
    if vogais[4] in palavras[c]:
        numu = palavras[c].count('U')
        print('U ' * numu)
