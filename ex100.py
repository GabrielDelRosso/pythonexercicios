import random

numeros = []


def sorteia(lista):
    for c in range(0, 5):
        sortear = random.randint(1, 10)
        lista.append(sortear)
    return lista


sorteia(numeros)
print(numeros)
