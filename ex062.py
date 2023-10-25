primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razao da P.A.: '))
termos = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while termos < total:
        termo = primeiro + (razao * termos)
        print(termo, end='')
        print(' => ', end='')
        termos = termos + 1
    print('PAUSA')
    mais = int(input('Quantoos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
