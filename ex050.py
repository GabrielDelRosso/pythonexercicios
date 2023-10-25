#lista de numeros que vai ser usada
numeros = []
numeros_par = []
#preenchimento da lista de numeros que vai ser usada
for c in range(0, 6):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
#numeros que foram capiturados pelo input
print(numeros)
#verificação se é par ou não
for c in range(0, 6):
    par = numeros[0+c] % 2
    if par == 0:
        numeros_par.append(numeros[0+c])
        print('O numero {} é par.'.format(numeros[0+c]))
print(numeros_par)
print('A soma de todos os números pares é {}.'.format(sum(numeros_par)))
