def leiaint():
    while True:
        n = input('Digite um número: ')
        if n.isnumeric():
            break
        else:
            print('\033[1:31mERRO! Digite um número inteiro!\033[m')
    print(f'O {n} é um número.')


leiaint()
