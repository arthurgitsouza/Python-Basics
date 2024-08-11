valores = tuple(int(input('Digite valores: ')) for c in range(1, 5))

print(f'O número nove aparece {valores.count(9)} vezes')

if 3 in valores:
    print(f'O valor 3 foi digitado pela primeira vez na {valores.index(3) + 1}ª posição')
else:
    print('Não foi digitado o valor 3')

print('Valores pares digitados foram:', end=' ')
valores_pares = [n for n in valores if n % 2 == 0]
print(valores_pares)
