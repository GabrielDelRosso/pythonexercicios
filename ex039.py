#import datetime
import time
birth = int(input('Digite o seu ano de nascimento: ')) #ano que nasceu
time = time.localtime() #data atual
army = time[0] - birth #calculo do nascimento
if army < 18:
    print('Seu dia de alistamento ainda não chegou! Aproveite!')
    print('Faltam {} ano(s) para o seu alistamento.'.format(18 - army))
elif army == 18:
    print('Seu ano de alistamento chegou! Boa sorte!')
else:
    print('Seu alistamento está atrasado! Vai sofrer!')
    print('Seu alistamento está {} ano(s) atrasado.'.format(army - 18))
