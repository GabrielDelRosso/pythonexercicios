valores = [[], []]
for c in range(0, 7):
    pegar_valores = int(input(f'Digite o {c+1}o número inteiro: '))
    pegar_valores_teste = pegar_valores % 2
    if pegar_valores_teste == 0:
        valores[0].append(pegar_valores)
    else:
        valores[1].append(pegar_valores)
print('=' * 50)
print(f'Os valores digitados foram: {valores}.')
valores[0].sort()
valores[1].sort()
print(f'Os valores pares em ordem crescente são: {valores[0]}.')
print(f'Os valores ímpares em ordem crescente são: {valores[1]}.')
print('=' * 50)
