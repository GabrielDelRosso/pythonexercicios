expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        pilha.append('(')
pilha_comprimento = len(pilha)
pilha_comprimento_par = pilha_comprimento % 2
if pilha_comprimento_par == 0:
    print('A expressão inserida é válida!')
else:
    print('A expressão inserida é inválida!')
