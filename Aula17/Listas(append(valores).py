valores = []
valores.append(9)
valores.append(8)
valores.append(7)

for v in valores:
    print(f'{v}',)

for c, v in enumerate(valores+1):
    print(f'Encontrei {v} na posição {c}!')