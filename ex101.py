import datetime


def voto(ano):
    """
    > Função feita para determinar se um indivíduo deve votar ou não.
    :param ano: ano de nascimento do individuo
    :return:
    """
    ano_atual = datetime.datetime.now().year
    votar = ano_atual - ano
    if votar < 18:
        print(f'Voto negado! Com {votar} anos é menor de idade.')
    elif votar < 65:
        print(f'Voto liberado! Com {votar} anos é obrigatório!')
    else:
        print(f'Voto opcional! Com {votar} é opcional o voto.')


# Programa Principal
pegar = int(input('Em que ano você nasceu? '))
voto(pegar)
