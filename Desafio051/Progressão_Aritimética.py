print('='*50)
print('              10 TERMOS DE UMA PA')
print('='*50)
pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = pt + (10 - 1) * razao
for i in range(pt, decimo_termo + razao, razao):
    print(i, end = ' ')
print('---- Acabou! ')
'''A progressão aritmética nada mais é que uma contagem e a razão é "passo" para o python, ou seja, é o número de "pulos".'''