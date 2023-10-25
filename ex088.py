import random
print('=' * 30)
print('SORTEAR JOGOS PARA A MEGA SENA')
print('=' * 30)
jogos = int(input('Quantos jogos você deseja sortear? '))
jogos_gerados = []
numeros = 6
numeros_gerados = []
for c in range(0, jogos):
    while len(numeros_gerados) < 6:
        gerar = random.randint(1, 60)
        if gerar not in numeros_gerados:
            numeros_gerados.append(gerar)
    numeros_gerados.sort()
    jogos_gerados.append(numeros_gerados[:])
    numeros_gerados.clear()
for f in range(0, jogos):
    print(jogos_gerados[f])
print('=' * 30)
print('{:^30}'.format('PALPITES GERADOS'))
print('=' * 30)
