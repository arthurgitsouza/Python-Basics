num = [0, 1, 2, 3]
letras = ['a', 'b']
num.pop(1)
num.remove(2) #Essa função elimina a váriavel que você colocar dentro dela
letras.remove('b')
print(letras)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

print(f'Essa lista tem {len(num)} elementos!')