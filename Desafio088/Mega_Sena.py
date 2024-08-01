from random import randint
op = int(input(('Quantos jogos você quer que eu sorteie? ')))
print(f'{"SOTEANDO " + str(op) + " JOGOS":=^40}')
for j in range(1, op+1):
    cont = 0
    jogo = []
    while len(jogo) < 6:
        num = randint(0, 60)
        if num not in jogo:
            jogo.append(num)
    print(f'Jogo {j}: {sorted(jogo)}')


