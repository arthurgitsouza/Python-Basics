n = int(input('Digite um número para você ver sua tabuada: '))
for m in range(1, 11):
    mult =  n * m
    print('{} x {} = {}'.format(n, m, mult))