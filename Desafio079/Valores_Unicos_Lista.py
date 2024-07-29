valores = []
while True:
    n = (int(input('Digite um valor:')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não adicionarei esse valor!')
    op = str(input('Quer continuar? [S/N] ')).strip()[0]
    while op not in 'SsNn':
        print('Opção inválida, por favor escolha entre S ou N!')
        op = str(input('Quer continuar? [S/N] ')).strip()[0]
    if op in 'Nn':
        break
print(f'Você digitou os valores {sorted(valores)}')