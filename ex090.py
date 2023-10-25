aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

if aluno['media'] < 6:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'
print(aluno)
print('=' * 30)
print(f'O nome do aluno é {aluno["nome"]}.')
print(f'A média do aluno é {aluno["media"]}.')
print(f'A situação do aluno é {aluno["situacao"]}.')
print('=' * 30)
