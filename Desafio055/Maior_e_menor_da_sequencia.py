maiorpeso = 0
menorpeso = 0
for pess in range(1, 6):
    p = float(input('Peso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        maiorpeso = pess
        menorpeso = pess
    else:
        if p > maiorpeso:
            maiorpeso = p
        if p < menorpeso:
            menor = p
print('O maior peso lido foi de {}Kg'.format(maiorpeso))
print('O menor peso lido foi de {}Kg'.format(menorpeso))
 