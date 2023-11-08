def aumentar(n=0, taxa=0, formato=False):
    aumento = n + (n*(taxa/100))
    return aumento if formato is False else moeda(aumento)


def diminuir(n=0, taxa=0, formato=False):
    diminui = n - (n*(taxa/100))
    return diminui if formato is False else moeda(diminui)


def dobro(n=0, formato=False):
    dobrar = 2 * n
    return dobrar if formato is False else moeda(dobrar)


def metade(n=0, formato=False):
    dividir = n / 2
    return dividir if formato is False else moeda(dividir)


def moeda(valor=0.0, tipo='R$'):
    return f'{tipo}{valor:.2f}'.replace('.', ',')
