maior = 0
homem = 0
mulher_20 = 0
continuar = 'S'
print('=' * 30)
print('CADASTRE UMA PESSOA')
print('=' * 30)
while continuar == 'S':
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior = maior + 1
    if sexo == 'M':
        homem = homem + 1
    if idade < 20 and sexo == 'F':
        mulher_20 = mulher_20 + 1
    continuar = str(input('Você deseja seguir cadastrando? [S/N] ')).strip().upper()[0]
print('=' * 30)
print(f'O número de pessoas com mais de 18 anos é: {maior}.')
print(f'O número de homens cadastrados é: {homem}.')
print(f'o número de mulheres menores de 20 anos é: {mulher_20}.')
print('=' * 30)
