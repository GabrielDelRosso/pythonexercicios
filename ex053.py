frase = str(input('Digite uma frase: '))
invertida = ''
print(len(frase))
for letra in range(len(frase) -1 , -1, -1):
    invertida = invertida + frase[letra]
print(invertida)