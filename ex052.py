numero = int(input('Digite um número inteiro: '))
print(numero)

numero_cond_1 = numero % 1
print(numero_cond_1)

numero_cond_2 = numero % numero
print(numero_cond_2)

numero_cond_3 = []
for c in range(2, 10):
    numero_cond_3_test = numero % c
    numero_cond_3.append(numero_cond_3_test)
print(numero_cond_3)

numero_cond_3_count = numero_cond_3.count(0)
print(numero_cond_3_count)

if numero >= 10:
    if numero_cond_3_count >= 1:
        numero_cond_3_bol = True
        print(numero_cond_3_bol)
    else:
        numero_cond_3_bol = False
        print(numero_cond_3_bol)
else:
    if numero_cond_3_count >= 2:
        numero_cond_3_bol = True
        print(numero_cond_3_bol)
    else:
        numero_cond_3_bol = False
        print(numero_cond_3_bol)

if numero_cond_1 == 0 and numero_cond_2 == 0 and numero_cond_3_bol == False:
    print('O número {} é PRIMO!'.format(numero))
else:
    print('O número {} NÃO É PRIMO!'.format(numero))
