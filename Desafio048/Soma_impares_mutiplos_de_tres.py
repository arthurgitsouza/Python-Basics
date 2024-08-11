soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i #Aqui a variavel soma que recebeu 0 vai ser somada com todos os numeros listados na variavel i!
print('A soma é de {}!'.format(soma))
 