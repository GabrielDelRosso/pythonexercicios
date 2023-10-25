primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razao da P.A.: '))
termos = 0
while termos < 10:
    termo = primeiro + (razao * termos)
    print(termo, end='')
    print(' => ', end='')
    termos = termos + 1
print('FIM DA P.A.')
