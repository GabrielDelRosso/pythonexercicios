m = float(input('Escreva o valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dec = m * 10
cent = m * 100
mili = m * 1000
print('{:>10}'.format('='))
print('O valor em m era: {}.\nSeus múltiplos são:\nDecâmetro: {}.\nHectômetro: {}.\nQuilômetro: {}.'.format(m, dam, hm, km))
print('=====')
print('O Valor em m era: {}.\nSeus submúltiplos são: \nDecímetro: {}.\nCentímetro: {}.\nMilímetro: {}.'.format(m, dec, cent, mili))
