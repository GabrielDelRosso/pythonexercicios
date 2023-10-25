while True:
    n = str(input('Digite um número para saber sua tabuada: '))
    if '-' in n:  #era só colocar if <0
        print('Valor inválido!')
        break
    n = int(n.replace('-', ''))
    print('A tabuada do número {} é:'.format(n))
    for c in range(1, 11):
        print('{} x {} = {}.'.format(n, c, c*n))
print('Programa encerrado!')
