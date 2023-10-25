lista_completa = []
lista_provisoria = []

while True:
    print('=' * 30)
    nome = str(input('Digite o nome do aluno: '))
    lista_provisoria.append(nome)
    nota1 = float(input('Digite a primeira nota do aluno: '))
    lista_provisoria.append(nota1)
    nota2 = float(input('Digite a segunda nota do aluno: '))
    lista_provisoria.append(nota2)
    lista_completa.append(lista_provisoria[:])
    lista_provisoria.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('=' * 30)
    if continuar == 'N':
        break

for c in range(0, len(lista_completa)):
    media = (lista_completa[c][1] + lista_completa[c][2]) / 2
    print(f'A média do aluno {c} foi {media}.')

while True:
    visualizar = int(input('Para visualizar as notas do aluno digite seu número (Para sair digite 999): '))
    if visualizar == 999:
        break
    else:
        print(f'As notas do aluno número {visualizar} foram {lista_completa[visualizar][1]} e {lista_completa[visualizar][2]}.')

print('Fim do programa!')