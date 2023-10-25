jogadores = list()
jogadores_individual = dict()

while True:
    jogadores_individual['nome'] = str(input('Digite o nome do jogador: '))
    jogadores_individual['partidas'] = int(input('Quantas partidas o jogador jogou? '))

    gols_partidas = []
    for c in range(0, jogadores_individual['partidas']):
        gols = int(input(f'Quantos gols ele fez na {c+1} partida? '))
        gols_partidas.append(gols)

    jogadores_individual['gols'] = gols_partidas
    jogadores_individual['total'] = sum(gols_partidas)
    jogadores.append(jogadores_individual.copy())
    jogadores_individual.clear()

    continuar = str(input('Deseja continuar cadastrando? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break


print('=' * 50)
print('{:<10}'.format('cod'), end='')
print('{:<15}'.format('nome'), end='')
print('{:<15}'.format('gols'), end='')
print('{:<10}'.format('total'))
print('=' * 50)
for c in range(0, len(jogadores)):
    print('{:<10}'.format(c), end='')
    print('{:<15}'.format(jogadores[c]["nome"]), end='')
    print(f'{jogadores[c]["gols"]}', end='')
    print('{:^15}'.format(jogadores[c]["total"]))
print('=' * 50)
while True:
    mostrar_jogador = int(input('Deseja visualizar os dados de qual jogador? [999 para parar] '))
    print(f'Dados do jogador {jogadores[mostrar_jogador]["nome"]}: ')
    for c in range(0, len(jogadores[mostrar_jogador]['gols'])):
        print(f'No jogo {c+1} fez {jogadores[mostrar_jogador]["gols"][c]} gols.')
