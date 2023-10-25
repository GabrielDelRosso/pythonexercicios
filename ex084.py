dados = []
continuar = 'S'
dados_pegar = []
while continuar == 'S':
    dados_pegar.append(str(input('Digite o nome da pessoa: ')))
    dados_pegar.append(float(input('Digite o peso da pessoa: ')))
    dados.append(dados_pegar[:])
    dados_pegar.clear()
    continuar = str(input('Deseja continuar cadastrando? [S/N] ')).strip().upper()[0]
pessoas = len(dados)
print('=' * 30)
print(f'Foram cadastradas {pessoas} pessoas.')
print('=' * 30)
pesos = []
for p in range(0, pessoas):
    pesos.append(dados[p][1])
pesos_max = max(pesos)
pesos_min = min(pesos)
lista_pesados = []
lista_leves = []
for c in range(0, len(dados)):
    if dados[c][1] == pesos_max:
        lista_pesados.append(dados[c])
    elif dados[c][1] == pesos_min:
        lista_leves.append(dados[c])
print(f'O maior peso foi: {pesos_max}kg.')
pesados_print = []
for c in range(0, len(lista_pesados)):
    pesados_print.append(lista_pesados[c][0])
print(f'As pessoas com o maior peso foram: {pesados_print}.')
print('=' * 30)
print(f'O menor peso foi: {pesos_min}kg.')
leves_print = []
for c in range(0, len(lista_leves)):
    leves_print.append(lista_leves[c][0])
print(f'As pessoas com o menor peso foram: {leves_print}.')
print('=' * 30)
