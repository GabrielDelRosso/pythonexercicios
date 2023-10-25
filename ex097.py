def escreva(*txt):
    print('=' * (len(*txt) + 2))
    print(*txt)
    print('=' * (len(*txt) + 2))


parametro = str(input('Digite algo: '))
escreva(parametro)
