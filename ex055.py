weight = []

for c in range(1, 6):
    readweight = float(input('Digite o peso da {}° pessoa: '.format(c)))
    weight.append(readweight)
print('Os valores digitados são: {}.'.format(weight))
print('O maior valor é: {}kg.'.format(max(weight)))
print('O menor valor é: {}kg.'.format(min(weight)))
