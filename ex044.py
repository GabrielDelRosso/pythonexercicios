print('LOJA DO GABRIEL')
compras = float(input('Qual o valor das compras?R$'))
print('FORMAS DE PAGAMENTO')
print('[1] à vista em dinheiro/cheque.')
print('[2] à vista cartão.')
print('[3] 2x no cartão.')
print('[4] 3x ou mais no cartão.')
forma = int(input('Qual a forma de pagamento?'))
if forma == 1:
    forma1desc = compras * 0.1
    forma1 = compras - forma1desc
    print('O valor da compra é R${}, com o desconto de 10% fica R${}.'.format(compras, forma1))
elif forma == 2:
    forma2desc = compras * 0.05
    forma2 = compras - forma2desc
    print('O valor da compra é R${}, com o desconto de 5% fica R${}.'.format(compras, forma2))
elif forma == 3:
    print('O valor da compra é R${}.'.format(compras))
elif forma == 4:
    forma4acres = compras * 0.20
    forma4 = compras + forma4acres
    print('O valor da compra é R${}, com os juros de 20% fica R${}.'.format(compras, forma4))
else:
    print('ERRO! Forma de pagamento não encontrada! Tente novamente.')
