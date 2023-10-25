valores = ((int(input('Digite um número: '))), (int(input('Digite um número: '))),
           (int(input('Digite um número: '))), (int(input('Digite um número: '))))
print(f'Os valores digitados foram {valores}.')
if 9 in valores:
    nove = valores.count(9)
    print(f'O valor 9 apareceu {nove} vezes.')
if 3 in valores:
    tres = valores.index(3)
    print(f'O valor 3 apareceu pela primeira vez na posição {tres + 1}.')
print('Os valores pares são: ', end='')
for valor in range(0, 4):
    par = valores[valor] % 2
    if par == 0:
        print(valores[valor], ' ',  end='')
