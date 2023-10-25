import random

numeros = dict()

numeros['jogador1'] = random.randint(1, 6)
numeros['jogador2'] = random.randint(1, 6)
numeros['jogador3'] = random.randint(1, 6)
numeros['jogador4'] = random.randint(1, 6)

print('Números sorteados: ')
for j, n in numeros.items():
    print(f'O {j} tirou {n}.')

print('Ranking de colocados:')
for i in sorted(numeros, key=numeros.get, reverse=True):
    print(f'O {i} tirou {numeros[i]}.')
