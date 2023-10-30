def ficha(n=0, g=0):
        nome = str(input('Digite o nome do jogador: '))
        gols = str(input('Digite quantos gols o jogador fez: '))
        if nome == '' and gols == '':
            print(f'O jogador <desconhecido> fez <desconhecido> gols no campeonato.')
        elif nome == '':
            print(f'O jogador <desconhecido> fez {gols} gols no campeonato.')
        elif gols == '':
            print(f'O jogador {nome}, fez <desconhecido> gols no campeonato.')
        else:
            print(f'O jogador {nome}, fez {gols} gols no campeonato.')


ficha()
