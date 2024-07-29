valores = []
cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    cont += 1
    op = str(input('Quer continuar? [S/N]')).strip()[0]
    while op not in 'SsNn':
        print('Opção inválida! Tente novamente, recebe apenas S ou N.')
        op = str(input('Quer continuar? [S/N]')).strip()[0]
    if op in 'Nn':
        valores.sort(reverse=True)
        break
print(f'Você digitou {cont} elementos'   )
print(f'Os valores em ordem decrescente são {valores}')