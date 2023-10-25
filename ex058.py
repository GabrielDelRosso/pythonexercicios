import random
import time
cont = 1
num = int(input('Digite um número inteiro entre 0 e 10: '))
num_random = random.randint(0, 10)
print('CARREGANDO...')
time.sleep(1)
if num == num_random:
    print('Você acertou! O número que voocê escolheu foi {} e o número escolhido pela máquina foi {}.'.format(num, num_random))
    print('Você precisou de {} tentativas.'.format(cont))
else:
    print('Você errou! Tente novamente!')
    while num != num_random:
        cont = cont + 1
        num = int(input('Digite um número inteiro entre 0 e 10: '))
        if num == num_random:
            print('CARREGANDO...')
            time.sleep(1)
            print('Você acertou! O número que você escolheu foi {} e o número selecionado pela máquina foi {}.'.format(num, num_random))
            print('Você precisou de {} tentativas.'.format(cont))
        else:
            print('CARREGANDO...')
            time.sleep(1)
            print('Você errou! Tente novamente!')
