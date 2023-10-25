primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
for c in range(0, 10):
    progressao = primeiro + (razao*c)
    print(progressao)
