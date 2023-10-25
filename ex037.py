num = int(input('Digite um número inteiro para ser convertido: '))
print('Escolha uma base para que a conversão seja realizada: ')
print('1. Binário.')
print('2. Octal.')
print('3. Hexadecimal.')
option = int(input('Digite uma das opções acima: '))
if option == 1:
    binario = bin(num)
    print(binario[2:])
elif option == 2:
    octal = oct(num)
    print(octal[2:])
elif option == 3:
    hexa = hex(num)
    print(hexa[2:])
else:
    print('Opção inválida.')
