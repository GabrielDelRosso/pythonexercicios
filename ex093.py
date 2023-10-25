jogador = dict()
jogador['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

gols_lista = []
for c in range(0, partidas):
    gols = int(input(f'Quantos gols o jogador fez na {c+1} partida? '))
    gols_lista.append(gols)
jogador['gols'] = gols_lista

gols_total = sum(gols_lista)
jogador['total'] = gols_total

print('=' * 40)
print(jogador)
print('=' * 40)
print(f'O campo nome tem valor {jogador["nome"]}.')
print(f'O campo gols tem valor {jogador["gols"]}.')
print(f'O campo total tem valor {jogador["total"]}.')
print('=' * 40)
for p in range(0, partidas):
    print(f'Na partida {p+1}, fez {jogador["gols"][p]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print('=' * 40)
