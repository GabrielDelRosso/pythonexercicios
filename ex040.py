n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) / 2
print('Quem tirou {} e {}, tem a média {}.'.format(n1, n2, m))
if m < 5.0:
    print('Você foi reprovado!')
elif m <= 6.9:
    print('Você está de recuperação!')
else:
    print('Você está aprovado!')
