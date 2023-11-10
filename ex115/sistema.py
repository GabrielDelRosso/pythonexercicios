from ex115.lib.interface import *

cabecalho('Sistema Arquivo v1.0')
while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Finalizando o sistema!')
        break
    else:
        print('ERRO! Digite uma opção válida!')

