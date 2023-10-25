print('''======
SEQUÊNCIA DE FIBONACCI
======''')
n = int(input('Quantos termos da Sequência de Fibonacci você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 10)
print('{} => {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' => {}'.format(t3), end='')
    cont = cont + 1
    t1 = t2
    t2 = t3
print(' => FIM')
print('~' * 10)
