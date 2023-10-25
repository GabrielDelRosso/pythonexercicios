lista_pessoas = list()
dicionario_pessoas = dict()

while True:
    dicionario_pessoas['nome'] = str(input('Digite o nome: '))
    dicionario_pessoas['sexo'] = str(input('Digite o Sexo [M/F]: ')).upper()
    dicionario_pessoas['idade'] = int(input('Digite a idade: '))
    dicionario_pessoas_copia = dicionario_pessoas.copy()
    lista_pessoas.append(dicionario_pessoas_copia)
    dicionario_pessoas.clear()
    continuar = str(input('Deseja continuar cadastrando? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Foram cadastradas {len(lista_pessoas)} pessoas.')

# media de idade
idades = []
for c in range(0, len(lista_pessoas)):
    idades.append(lista_pessoas[c]['idade'])
idades_media = sum(idades)/len(lista_pessoas)
print(f'A média de idade das pessoas cadastradas foi {idades_media}.')

# mulheres
mulheres = []
for c in range(0, len(lista_pessoas)):
    if lista_pessoas[c]['sexo'] == "F":
        mulheres.append(lista_pessoas[c]['nome'])
print(f'As mulheres são: {mulheres}.')

