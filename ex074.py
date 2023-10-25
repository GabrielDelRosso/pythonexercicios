import random
numeros_aleatorios = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
                      random.randint(0, 10), random.randint(0, 10))
print('=' * 50)
print(f'Os números gerados foram {numeros_aleatorios}.')
numeros_menor = min(numeros_aleatorios)
print(f'O menor número da tupla é {numeros_menor}.')
numeros_maior = max(numeros_aleatorios)
print(f'O maior número da tupla é {numeros_maior}.')
print('=' * 50)
