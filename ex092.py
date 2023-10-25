import datetime
dados = dict()

dados['nome'] = str(input('Digite o nome: '))
dados['nascimento'] = int(input('Digite o ano de nascimento: '))
dados['carteira'] = int(input('Digite o n da carteira de trabalho (0 não tem): '))
if dados['carteira'] != 0:
    dados['ano'] = int(input('Digite o ano da contratação: '))
    dados['salario'] = float(input('Digite o salário: '))

idade = datetime.date.today().year - dados['nascimento']

print('=' * 40)
print(f'O nome tem valor: {dados["nome"]}.')
print(f'A idade tem valor: {idade}.')
print(f'A carteira de trabalho tem valor: {dados["carteira"]}.')
if dados["carteira"] != 0:
    contratacao_idade = idade - (datetime.date.today().year - dados['ano'])
    aposentadoria_idade = contratacao_idade + 35
    print(f'A contratação tem valor: {dados["salario"]}.')
    print(f'A aposentadoria tem valor: {aposentadoria_idade}.')
print('=' * 40)
