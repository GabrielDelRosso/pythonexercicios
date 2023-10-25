somaidade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher_20 = 0
for p in range(1, 5):
    print('CADASTRO DA {}° PESSOA'.format(p))
    nome = str(input('Digite o nome da {}° pessoa: '.format(p))).strip()
    idade = int(input('Digite a idade da {}° pessoa: '.format(p)))
    sexo = str(input('Digite o sexo(M ou F) da {}° pessoa: '.format(p))).strip().lower()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in "Ff" and idade < 20:
        tot_mulher_20 = tot_mulher_20 + 1
media_idade = somaidade/4
print('A média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(tot_mulher_20))
