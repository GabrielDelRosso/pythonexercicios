def pyhelp():
    while True:
        print('\033[1:34:40m=\033[m'*30)
        print('{:^30}'.format('\033[1:34:40mSISTEMA DE AJUDA PyHELP!\033[m'))
        print('\033[1:34:40m=\033[m'*30)
        func = str(input('\033[1:31:40mDigite a função ou biblioteca: \033[m').strip().lower())
        if func == 'fim':
            break
        else:
            print(help(func))
    print('Fim do programa!')
    return


pyhelp()
