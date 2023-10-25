nome = str(input('Digite o seu nome completo: ')).strip()
nomeupper = nome.upper()
nomelower = nome.lower()
nomeletras = nome.replace(' ', '')
nomeletrascount = len(nomeletras) #.format(len(nome) - nome.count(''))
nomesplit = nome.split()

print(nomeupper)
print(nomelower)
print(nomeletrascount)
print(len(nomesplit[0])) #posso contar até o primeiro espaço
