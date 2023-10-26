import time


def maior(*num):
    valor_alto = max(*num)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        time.sleep(0.5)
    print()
    print(f'O maior valor é {valor_alto}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
