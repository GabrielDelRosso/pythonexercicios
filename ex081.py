lista_numeros = []
continuar = 'S'
while continuar == 'S':
    lista_numeros.append(int(input('Digite um número inteiro: ')))
    continuar = str(input('Deseja continuar cadastrando números? [S/N]')).strip().upper()[0]
print('=' * 30)
print(f'Foram digitados {len(lista_numeros)} números.')
lista_numeros.sort(reverse=True)
print(f'A lista de valores digitada em ordem decrescente é: {lista_numeros}.')
if 5 in lista_numeros:
    print('O número 5 está presente na lista!')
else:
    print('O número 5 não está presente na lista!')
print('=' * 30)
