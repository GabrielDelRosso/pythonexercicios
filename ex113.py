def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[1:31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1:31mERRO! Entrada de dados interrompida pelo usuário!\033[m')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[1:31mERRO! Por favor, digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1:31mERRO! Entrada de dados interrompida pelo usuário!\033[m')
            continue
        else:
            return n


num = leiaint('Digite um número inteiro: ')
print(f'O valor digitado foi {num}.')
num2 = leiafloat('Digite um número real: ')
print(f'O valor digitado foi {num2}.')
