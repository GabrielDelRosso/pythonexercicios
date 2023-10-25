import math
cateto1 = float(input('Qual o tamanho do cateto oposto? '))
cateto2 = float(input('Qual o tamanho do cateto adjacente? '))
hipotenusa = math.hypot(cateto1, cateto2)
print('=====')
print('O tamanho da hipotenusa é {:.2f}.'.format(hipotenusa))
print('=====')
