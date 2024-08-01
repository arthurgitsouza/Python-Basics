valores = []
lista0 = []
lista1 = []
lista2 = []
soma = 0
maior_segunda_coluna = 0
for l in range(0,3):
    valores.append(int(input(f'Digite um valor para [0, {l}]: ')))
    if l == 0:
        lista0.append(valores[0])
        if valores[0] % 2 == 0:
            soma += valores[0]
    elif l == 1:
        lista1.append(valores[1])
        if valores[1] % 2 == 0:
            soma += valores[1]
    else:
        lista2.append(valores[2])
        if valores[2] % 2 == 0:
            soma += valores[2]
for v in range(0, 3):
    valores.append(int(input(f'Digite um valor para [1, {v}]: ')))
    if v == 0:
        lista0.append(valores[3])
        maior_segunda_coluna = valores[3]
        if valores[3] % 2 == 0:
            soma += valores[3]
    elif v == 1:
        lista1.append(valores[4])
        if valores[4] % 2 == 0:
            soma += valores[4]
        if valores[4] > valores[3]:
            maior_segunda_coluna = valores[4]
    else:
        lista2.append(valores[5])
        if valores[5] % 2 == 0:
            soma += valores[5]
        if valores[5] > valores[3] and valores[5] > valores[4]:
            maior_segunda_coluna = valores[5]
for u in range(0, 3):
    valores.append(int(input(f'Digite um valor para [2, {u}]: ')))
    if u == 0:
        lista0.append(valores[6])
        if valores[6] % 2 == 0:
            soma += valores[6]
    elif u == 1:
        lista1.append(valores[7])
        if valores[7] % 2 == 0:
            soma += valores[7]
    else:
        lista2.append(valores[8])
        if valores[8] % 2 == 0:
            soma += valores[8]
soma_terceira_coluna = valores[2] + valores[5] + valores[8]
print('-'*30)
print(lista0)
print(lista1)
print(lista2)
print('-'*30)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda coluna é {maior_segunda_coluna}')
