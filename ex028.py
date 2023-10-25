import random
import time
num = int(input('Digite um numero aleatório entre 0 e 5: '))
num_random = random.randint(0, 5)
print('PROCESSANDO...')
time.sleep(1)
if num == num_random:
    print('Você acertou! O número aleatório era {}, e o número que você digitou é {}.'.format(num_random, num))
else:
    print('Você errou! O número aleatório era {}, e o número que você digitou é {}.'.format(num_random, num))
