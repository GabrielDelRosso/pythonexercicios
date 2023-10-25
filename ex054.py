nascimento = []
idade = []
maiores = []
menores = []

for c in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    nascimento.append(ano)
print(nascimento)

for i in nascimento:
    atual = 2023 - i
    idade.append(atual)
print(idade)

for d in idade:
    if d >= 18:
        maiores.append(d)
    else:
        menores.append(d)
print(maiores)
print(menores)
print('O número de indivíduos maiores de idade é {}.'.format(len(maiores)))
print('O número de indivíduos menores de idade é {}.'.format(len(menores)))
