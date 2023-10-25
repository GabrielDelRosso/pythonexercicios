n = 0
cont = 0 - 1
sum = 0 - 999
while n != 999:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    cont = cont + 1
    sum = sum + n
print('Foram digitados {} números e sua soma é {}.'.format(cont, sum))
