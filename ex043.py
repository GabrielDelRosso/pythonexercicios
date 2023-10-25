peso = float(input('Qual o seu peso atual? Em kgs: '))
altura = float(input('Qual a sua altura? Em metros: '))
imc = peso/altura**2
print('Seu imc é {:.2f}kg/m²'.format(imc))
if imc < 18.5:
    print('Sua classificação é: \033[31mAbaixo do peso\033[m.')
elif imc < 25:
    print('Sua classificação é: \033[32mPeso Ideal\033[m.')
elif imc < 30:
    print('Sua classificação é: \033[31mSobrepeso\033[m.')
elif imc < 40:
    print('Sua classificação é \033[31mObesidade\033[m.')
else:
    print('Sua classificação é \033[31mObesidade Mórbida\033[m.')
