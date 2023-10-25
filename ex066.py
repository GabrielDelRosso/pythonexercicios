n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um número inteiro [Digite 999 para parar]: '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print(f'A soma de {cont} números digitados foi {soma}.')
