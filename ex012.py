prod = float(input('Digite o valor do produto em R$: '))
desc = prod * 0.05
proddesc = prod - desc
print('=====')
print('O valor do produto é {:.2f}.\nO valor do desconto é {:.2f}.\nO valor do produto com o descomto aplicado é {:.2f}.'.format(prod, desc, proddesc))
print('=====')
