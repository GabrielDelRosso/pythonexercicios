def linha():
    print('=' * 30)


def area(largura, comprimento):
    area_terreno = l * c
    print(f'A area do terreno é {area_terreno}')


# Programa Principal
linha()
print('{:^30}'.format('Controle de Terrenos'))
linha()

l = float(input('Digite a LARGURA(m) do terreno: '))
c = float(input('Digite a ALTURA(m) do terreno: '))
area(l, c)

