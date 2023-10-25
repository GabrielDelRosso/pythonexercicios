total = 0
mais_de_1k = 0
barato = 0
barato_nome = ''
continuar = 'S'
cont = 0
while continuar == 'S':
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto em R$: '))
    total = total + preco
    cont = cont + 1
    if preco > 1000:
        mais_de_1k = mais_de_1k + 1
    if cont == 1:
        barato = preco
        barato_nome = produto
    if cont > 1:
        if preco < barato:
            barato = preco
            barato_nome = produto
    continuar = str(input('Deseja continuar cadastrando produtos? [S/N] ')).strip().upper()[0]
print(f'O total gasto na compra é de R${total}.')
print(f'{mais_de_1k} produtos custam mais de R$1000.')
print(f'O produto mais barato é: {barato_nome}.')
