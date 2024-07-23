print('='*40)
print(f'{'BANCO CEV':-^40}')
print('='*40)
valor = float(input('Que valor você quer sacar? R$'))
cont50 = cont20 = cont10 = cont1 = 0
while valor > 50:
    valor = valor - 50
    cont50 += 1
    while valor < 50 and valor >= 20:
        valor = valor - 20
        cont20 += 1
    while valor < 20 and valor >= 10:
        valor = valor - 10
        cont10 += 1
    while valor < 10 and valor > 0:
        valor = valor - 1
        cont1 += 1
    if valor == 0:
        break
if cont50 > 0:
        print(f'Total de {cont50} células de R$50,00.')
if cont20 > 0:
    print(f'Total de {cont20} células de R$20,00.')
if cont10 > 0:
    print(f'Total de {cont10} células de R$10,00.')
if cont1 > 0:
    print(f'Total de {cont1} células de R$1,00.')
print(f'{'Volte sempre ao BANCO CEV, Tenha um bom dia!':-^40}')