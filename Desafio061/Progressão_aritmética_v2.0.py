termo = int(input('Qual o 1° termo: '))
razao = int(input('Qual a razão: '))
c = 10
print(f'A PA de {termo} é:', end='')
while c > 0:
    print(f"{termo} > ", end="")
    termo += razao
    c -= 1
print('Acabou!')