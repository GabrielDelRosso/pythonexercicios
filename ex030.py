num = int(input('Digite um número inteiro: '))
numparimp = num % 2
if numparimp == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é ímpar!'.format(num))
