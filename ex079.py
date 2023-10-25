lista_numeros = []
continuar = 'S'
print('=' * 30)
print('{:^30}'.format('CADASTRO DE NÚMEROS'))
print('=' * 30)
while continuar == 'S':
    lista_numeros_recebe = int(input('Digite um número inteiro: '))
    if lista_numeros_recebe in lista_numeros:
        print('Esse número já está na lista!')
    else:
        lista_numeros.append(lista_numeros_recebe)
        print('Adicionado com sucesso!')
    continuar = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
    print('=' * 30)
print('Fim do programa!')
lista_numeros.sort()
print(f'Os números cadastrados foram: {lista_numeros}.')
print('=' * 30)
