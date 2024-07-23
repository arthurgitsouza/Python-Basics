print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
total_gasto = preço_maior_1000 = menor = cont = 0
barato = ''
while True:
    np = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    op = str(input('Quer continuar? [S/N]')).strip()[0]
    total_gasto += preço
    if preço > 1000:
        preço_maior_1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        produto_barato = np
    while op not in 'SsNn':
        print('Opção Inválida! Tente novamente.')
        op = str(input('Quer continuar? [S/N]')).strip()[0]
    if op in 'Nn':
        break
print(f'O total da compra foi {total_gasto}.')
print(f'Temos {preço_maior_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato é o {produto_barato} custa R${menor:.2f}')


    