import moeda

n = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}.')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}.')
print(f'Adicionando 10%, é {moeda.aumentar(n, 10, True)}.')
print(f'Diminuindo 10%, é {moeda.diminuir(n, 13, True)}.')
