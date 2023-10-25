import random
print('Pedra, Papel ou Tesoura!')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
jokenpo = int(input('Digite a sua jogada: '))
if jokenpo == 1:
    print('Você jogou Pedra!')
elif jokenpo == 2:
    print('Você jogou Papel!')
elif jokenpo == 3:
    print('Você jogou Tesoura!')
else:
    print('ERRO! Escolha uma opção válida!')
jokenpomaquina = random.randint(1, 3)
if jokenpomaquina == 1:
    print('A máquina jogou Pedra!')
elif jokenpomaquina == 2:
    print('A máquina jogou Papel!')
elif jokenpomaquina == 3:
    print('A máquina jogou Tesoura!')
if jokenpo == jokenpomaquina:
    print('Você e a máquina empataram, tente outra vez!')
elif jokenpo == 1 and jokenpomaquina == 3:
    print('Você venceu!')
elif jokenpo == 3 and jokenpomaquina == 2:
    print('Você venceu!')
elif jokenpo == 2 and jokenpomaquina == 1:
    print('Você venceu!')
else:
    print('Você perdeu!')
