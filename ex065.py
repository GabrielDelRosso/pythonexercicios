valores = []
continuar = 'S'
cont = 0
while continuar == 'S':
    valores.append(int(input('Digite um número inteiro: ')))
    cont = cont + 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
media = sum(valores) / cont
print('A média dos valores: {}, é {}.'.format(valores, media))
maior = max(valores)
menor = min(valores)
print('O maior valor entre os valores: {} é {}.'.format(valores, maior))
print('O menor valor entre os valores: {} é {}.'.format(valores, menor))
print('Fim do Programa!')
