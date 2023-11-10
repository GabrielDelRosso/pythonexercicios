from ex115.lib.interface import *
from time import sleep

cabecalho('Sistema Arquivo v1.0')
while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        cabecalho('Listar Pessoas')
    elif resposta == 2:
        cabecalho('Cadastrar Pessoas')
    elif resposta == 3:
        cabecalho('Finalizando o sistema!')
        break
    else:
        cabecalho('\033[33mERRO! Digite uma opção válida!\033[m')
    sleep(1)
