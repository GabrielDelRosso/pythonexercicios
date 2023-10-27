from random import randint


def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))


def somapar(lista):
    lista_pares =[]
    for c in range(0, 5):
        if lista[c] % 2 == 0:
            lista_pares.append(lista[c])
    print(sum(lista_pares))


numeros = []
sorteia(numeros)
print(numeros)
somapar(numeros)
