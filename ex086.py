matriz = [[], [], [], [], [], [], [], [], []]
matriz_pegar = 0
for c in range(0, 9):
    matriz_pegar = int(input(f'Digite o um valor para a matriz: '))
    matriz[c].append(matriz_pegar)
print(f'{matriz[0]}, {matriz[1]}, {matriz[2]}')
print(f'{matriz[3]}, {matriz[4]}, {matriz[5]}')
print(f'{matriz[6]}, {matriz[7]}, {matriz[8]}')
