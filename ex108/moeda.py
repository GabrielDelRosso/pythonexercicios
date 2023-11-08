def aumentar(n=0, taxa=0):
    aumento = n + (n*(taxa/100))
    return aumento


def diminuir(n=0, taxa=0):
    diminui = n - (n*(taxa/100))
    return diminui


def dobro(n=0):
    dobrar = 2 * n
    return dobrar


def metade(n=0):
    dividir = n / 2
    return dividir


def moeda(valor=0, tipo='R$'):
    return f'{tipo}{valor:.2f}'.replace('.', ',')
