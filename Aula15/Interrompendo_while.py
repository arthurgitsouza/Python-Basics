n = s = 0 
while True: #O True serve para criar um loop infinito!
    n = int(input('Digite um número: '))
    if n == 999:
        break #para o programa se o N for igual à 999!
    s += n
print(f'A soma vale {s}.')


'''n = s = 0
while n != 1000:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print(f'A soma vale {s}')'''