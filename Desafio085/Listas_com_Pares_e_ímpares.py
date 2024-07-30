valores = []
valores_pares = []
valores_impares = []
for v in range(1,8):
    valores.append(int(input(f'Digite o {v}° valor: ')))
for n in valores:
    if n % 2 == 0:
        valores_pares.append(n)
    else:
        valores_impares.append(n)
print(f'Os valores pares digitados foram: {sorted(valores_pares)}.')
print(f'Os valores ímpares digitados foram: {sorted(valores_impares)}')