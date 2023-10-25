lista_numeros = []
lista_numeros_par = []
lista_numeros_impar = []
while True:
    numeros = int(input('Digite um número: '))
    if numeros % 2 == 0:
        lista_numeros.append(numeros)
        lista_numeros_par.append(numeros)
    else:
        lista_numeros.append(numeros)
        lista_numeros_impar.append(numeros)
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Os números digitados foram: {lista_numeros}.')
print(f'Os números PARES digitados foram: {lista_numeros_par}.')
print(f'Os números ÍMPARES digitados foram: {lista_numeros_impar}.')
