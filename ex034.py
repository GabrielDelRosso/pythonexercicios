salario = float(input('Qual o seu salário? R$'))
if salario <= 1250:
    aumento1 = salario * 0.15
    salario_aumento1 = salario + aumento1
    print('O seu novo salário após o aumento é de: R${:.2f}.'.format(salario_aumento1))
else:
    aumento2 = salario * 0.10
    salario_aumento2 = salario + aumento2
    print('O seu novo salário após o aumento é de: R${:.2f}.'.format(salario_aumento2))
