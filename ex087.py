matriz = []
matriz_pegar = 0
for c in range(0, 9):
    matriz_pegar = int(input(f'Digite o um valor para a matriz: '))
    matriz.append(matriz_pegar)
print(f'{matriz[0]}, {matriz[1]}, {matriz[2]}')
print(f'{matriz[3]}, {matriz[4]}, {matriz[5]}')
print(f'{matriz[6]}, {matriz[7]}, {matriz[8]}')
pares = []
for i in range(0, 9):
    if matriz[i] % 2 == 0:
        pares.append(matriz[i])
pares_soma = sum(pares)
print(f'A soma de todos os valores pares digitados é {pares_soma}.')
soma_3_coluna = matriz[2] + matriz[5] + matriz[8]
print(f'A soma dos números da terceira coluna é {soma_3_coluna}.')
maior_2_linha = max(matriz[3], matriz[4], matriz[5])
print(f'O maior valor da segunda linha é {maior_2_linha}.')
