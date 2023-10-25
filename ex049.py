n = int(input('Digite um número para saber sua tabuada: '))
print('A tabuada do número {} é:'.format(n))
for c in range(1, 11):
    print('{} x {} = {}.'.format(n, c, c*n))
