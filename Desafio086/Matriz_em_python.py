valores = [] 
lista0 = []
 
for v in range(0,3):
    valores.append(int(input(f'Digite um valor para [0, {v}]: ')))
    '''if v == 0:
        lista0.append(valores[0])'''
for c in range(0,3):
    valores.append(int(input(f'Digite um valor para [1, {c}]: ')))
    '''if c == 0:
        lista0.append(valores[3])'''
for u in range(0,3):
    valores.append(int(input(f'Digite um valor para [2, {u}]: ')))
    '''if u == 0:
        lista0.append(valores[9])'''
while v == 0 and c == 0 and u == 0:
    lista0.append(valores[0])
print(lista0)