distance = int(input('Qual é a distância da sua viagem? '))
print('Você vai realizar uma viagem de {}km.'.format(distance))
if distance <= 200:
    print('O preço de sua viagem será: R${:.2f}.'.format(distance * 0.50))
else:
    print('O preço de sua viagem será: R${:.2f}.'.format(distance * 0.45))
