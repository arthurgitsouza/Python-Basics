valores = []
maior = 0
menor = 0
for v in range(5):
    valores.append(int(input(f'Digite um valor para a posição {v}:')))
    if v == 0:
        maior = menor = valores[v] #Se for o primeiro numero a ser lido.
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print('-'*40)
print(f'Você digitou os valores: {valores}')
print('-'*40)
for pos, v in enumerate(valores):
    if v == menor:
        print(f'O maior valor digitado foi {maior} na posição {pos}!')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'O menor valor digitado foi {menor} na posição {pos}!')