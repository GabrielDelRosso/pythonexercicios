lista_numeros = []
for d in range(0, 5):
    lista_termo = int(input(f'Digite o {d + 1}° número inteiro: '))
    if d == 0:
        lista_numeros.append(lista_termo)
    if lista_termo > lista_numeros[-1]:
        lista_numeros.append(lista_termo)
    else:
        cont = 0
        while cont < len(lista_numeros):
            if lista_termo <= lista_numeros[cont]:
                lista_numeros.insert(cont, lista_termo)
                break
            cont = cont + 1
print(f'Os valoroes digitados em ordem são: {lista_numeros}.')
# Sempre pensar que quando tu precisa observar termo por termo que está inserido em uma lista, tu pode usar um laço de repetição.
