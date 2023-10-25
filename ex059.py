opcao = 0
print('=' * 5, 'INSIRA OS NÚMEROS', '=' * 5)
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
print('=' * 5)
while opcao != 5:
    print('Escolha uma opção: ')
    print('1. Soma')
    print('2. Multiplicação')
    print('3. Maior número')
    print('4. Novos números')
    print('5. Sair do Programa.')
    opcao = int(input('Digite a opção que você deseja: '))
    if opcao == 1:
        soma = n1 + n2
        print('=' * 10)
        print('A soma entre os números {} e {} é {}.'.format(n1, n2, soma))
        print('=' * 10)
    elif opcao == 2:
        multiplo = n1 * n2
        print('=' * 10)
        print('O múltiplo entre os números {} e {} é {}.'.format(n1, n2, multiplo))
        print('=' * 10)
    elif opcao == 3:
        maior = max(n1, n2)
        print('=' * 10)
        print('O maior número entre {} e {} é {}.'.format(n1, n2, maior))
        print('=' * 10)
    elif opcao == 4:
        print('=' * 10)
        print('Insira novos valores: ')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print('=' * 10)
print('Programa finalizado!')
