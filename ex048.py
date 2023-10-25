multiplo = []
impares = []
for c in range(1, 501):
    m3 = c % 3
    if m3 == 0:
        multiplo.append(c)
print(multiplo)
for i in multiplo:
    imp = i % 2
    if imp != 0:
        impares.append(i)
print(impares)
soma_dos_impares = sum(impares)
num_impares = len(impares)
print(soma_dos_impares)
print(num_impares)
