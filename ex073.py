times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino', 'Athletico-PR',
         'Fortaleza', 'Atlético-MG', 'Cuiabá', 'São Paulo', 'Cruzeiro', 'Corinthians',
         'Internacional', 'Goiás', 'Bahia', 'Santos', 'Vasco da Gama', 'América-MG', 'Coritiba')
print('=' * 30)
print('{:^30}'.format('CAMPEONATO BRASILEIRO'))
print('=' * 30)
print('{:^30}'.format('CINCO PRIMEIROS'))
for time in range(0, 5):
    print(times[time])
print('=' * 30)
print('{:^30}'.format('ÚLTIMOS QUATRO'))
for time in range(16, 20):
    print(times[time])
print('=' * 30)
print('{:^30}'.format('TIMES EM ORDEM ALFABÉTICA'))
times_alfabeto = sorted(times)
for equipes in times_alfabeto:
    print(equipes)
print('=' * 30)
print('{:^30}'.format('POSIÇÃO DO GRÊMIO'))
gremio = times.index('Grêmio')
print(f'O Grêmio está na {gremio+1}ª posição.')
print('=' * 30)
