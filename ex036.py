#importando bibliotecas
import time
#Obtendo os dados necessários
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar a casa? '))
#Realizando as operações
prestacao = casa/(anos * 12)
prestacaomax = salario * 0.3
print('Analizando seu empréstimo...')
time.sleep(3)
#Analizando se é possível conceder o empréstimo
print('Para adquirir uma casa de R${:.2f}, em {:.2f} anos, o valor da prestação é de R${:.2f}.'.format(casa, anos, prestacao))
if prestacao <= prestacaomax:
    print('\033[32mO empréstimo foi liberado! Desfrute de sua nova casa!\033[m')
else:
    print('\033[31mO empréstimo foi negado!\033[m')
