def notas(*n, sit=False):
    """
    => Recebe uma série de notas e mostra quantas foram inseridas, a maior, a menor, a media e a situação se sit=True.
    :param n: notas
    :param sit: situação do aluno
    :return: dicionário com várias informações.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa Principal
resp = notas(7.5, 5.5, 9, 8.5, sit=True)
print(resp)
help(notas)
