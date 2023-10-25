velocity = float(input('Digite a velocidade do carro em km/h: '))
if velocity > 80.0:
    print('Você foi multado!')
    print('O valor da multa é de R${:.2f}.'.format((velocity - 80) * 7))
else:
    print('Você está dentro dos limites de velocidade!')
