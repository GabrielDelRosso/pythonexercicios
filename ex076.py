produtos = ('Cerveja Polar', '5', 'Cerveja Brahma Chopp', '8', 'Cerveja Original', '10', 'Batata Frita', '10',
            'Hambúrguer', '12', 'Amendoim', '5', 'Picadinho', '15', 'Chiclete', '2', 'Chocolate', '5',
            'Caipirinha', '10')
print('=' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('=' * 40)
for c in range(0, 20, 2):
    print('{:<20}'.format(produtos[c]), '{:>15}'.format('R$'), '{:>3}'.format(produtos[c+1]))
print('=' * 40)
