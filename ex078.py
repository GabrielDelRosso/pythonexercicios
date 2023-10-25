numeros = []
maior = 0
menor = 0
for n in range(0, 5):
    numeros.append(int(input(f'Digite um número inteiro na posição {n}: ')))
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]
print('=' * 30)
print(f'Você digitou os números {numeros}.')
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}... ', end='')
print()
# Tive um pouco de dificuldade nesse exercicio, vou tentar fazer ele outra vez no futuro.
