lado1 = float(input('Digite o tamanho do primeiro lado do triângulo: '))
lado2 = float(input('Digite o tamanho do segundo lado do triângulo: '))
lado3 = float(input('Digite o tamanho do terceiro lado do triângulo: '))
if lado1 + lado2 < lado3:
    print('As três retas inseridas podem formar um triângulo.')
else:
    print('As três retas inseridas não podem formar um triângulo.')
