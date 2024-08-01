valores = [] 
lista0 = []
lista1 = []
lista2 = []
for v in range(0,3):
    valores.append(int(input(f'Digite um valor para [0, {v}]: ')))
    if v == 0:
        lista0.append(valores[0])
    if v == 1:
        lista1.append(valores[1])
    if v == 2:
        lista2.append(valores[2])
for c in range(0,3):
    valores.append(int(input(f'Digite um valor para [1, {c}]: ')))
    if c == 0:
        lista0.append(valores[3])
    if c == 1:
        lista1.append(valores[4])
    if c == 2:
        lista2.append(valores[5])
for u in range(0,3):
    valores.append(int(input(f'Digite um valor para [2, {u}]: ')))
    if u == 0:
        lista0.append(valores[6])
    if u == 1:
        lista1.append(valores[7])
    if u == 2:
        lista2.append(valores[8])
print(lista0)
print(lista1)
print(lista2)