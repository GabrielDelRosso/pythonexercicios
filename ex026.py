frase = str(input('Digite uma frase de sua escolha: ')).strip()
frase_num_a = frase.lower().count('a')
print('A letra A aparece na frase: ')
print(frase_num_a)
frase_find_a = frase.lower().find('a')+1
print('A primeira posição que a letra A aparece na frase é: ')
print(frase_find_a)
frase_find_last_a = frase.lower().rfind('a')+1
print('A ultima posição que a letra A aparece na frase é:')
print(frase_find_last_a)
