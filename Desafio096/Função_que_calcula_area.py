def area(l, c):
    area = l * c
    print(f'A área de um terreno {l} x {c} é de {area}m²!')

print()
print('  Controle de Terrenos')
print('-'*30)
lag = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(lag, comp)