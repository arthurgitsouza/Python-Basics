print('='*40)
print(f'{'BANCO CEV':-^40}')
print('='*40)
valor = float(input('Que valor você quer casar? R$'))
cont = 0
while valor % 50 == 0:
    cont += 1
print(cont)