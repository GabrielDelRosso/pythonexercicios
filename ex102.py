def fatorial(n, show=False):
    """
    => Calcula o fatorial de um número.
    :param n: Número que se deseja o fatorial.
    :param show: Mostrar a conta ou não.
    :return: Retorna o fatorial do valor n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=False))
help(fatorial)