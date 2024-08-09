termo = int(input("Qual o 1º termo: "))
razao = int(input("Qual a razão: "))
c = 10
print(f"A PA de {termo} é:", end=" ")
while c != 0:
    while c > 0:
        print(f"{termo} > ", end="")
        termo += razao
        c -= 1
    print('PAUSA')
    c = int(input('\nQuantos termos você quer mostrar a mais? '))
print('Acabou!')