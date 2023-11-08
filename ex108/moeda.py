def aumentar(n, taxa):
    aumento = n + (n*(taxa/100))
    return aumento


def diminuir(n, taxa):
    diminui = n - (n*(taxa/100))
    return diminui


def dobro(n):
    dobrar = 2 * n
    return dobrar


def metade(n):
    dividir = n / 2
    return dividir


def moeda(valor):
    num = f'R$ {valor}'
    formata_num = num.replace('.', ',')
    return formata_num
