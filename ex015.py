km = float(input('Quantos km foram rodados pelo veículo? '))
dias = int(input('Quantos dias o carro ficou alugado? '))
precokm = km * 0.15
precodia = dias * 60
precototal = precokm + precodia
print('=====')
print('O valor total pelos km rodados é {:.2f}.'.format(precokm))
print('O valor total pelos dias alugados é {:.2f}.'.format(precodia))
print('O valor total do aluguel é {:.2f}.'.format(precototal))
print('=====')
