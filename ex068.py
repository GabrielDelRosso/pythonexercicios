import random
cont = 0
print('=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=' * 30)
while True:
    n = int(input('Digite um valor inteiro: '))
    paridade = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    computador = random.randint(1, 10)
    total = n + computador
    paridade_computador_usuario = total % 2
    paridade_computador_usuario_nome = ''
    if paridade_computador_usuario == 0:
        paridade_computador_usuario_nome = 'PAR'
    else:
        paridade_computador_usuario_nome = 'IMPAR'
    print(f'Você jogou {n}, o computador jogou {computador}, a soma dos dois números é {total}, um número {paridade_computador_usuario_nome}.')
    if paridade_computador_usuario == 0 and paridade == 'P':
        print('Você venceu!')
        cont = cont + 1
    elif paridade_computador_usuario != 0 and paridade == 'I':
        print('Você venceu!')
        cont = cont + 1
    else:
        print('Você perdeu!')
        break
print(f'Foram necessárias {cont} tentativas.')
print('=' * 30)
