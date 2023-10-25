side1 = float(input('Digite o primeiro lado do triângulo: '))
side2 = float(input('Digite o segundo lado do triângulo: '))
side3 = float(input('Digite o terceiro lado do triângulo: '))
print('O triângulo possui lados de valores: {}, {} e {}.'.format(side1, side2, side3))
if side1 > side2 + side3:
    print('O triângulo não existe!')
elif side2 > side1 + side3:
    print('O triângulo não existe!')
elif side3 > side1 + side2:
    print('O triângulo não existe!')
    quit()
if side1 == side2 == side3:
    print('O triângulo é equilátero!')
elif side1 != side2 != side3:
    print('O triângulo é escaleno!')
else:
    print('O triângulo é isósceles!')
