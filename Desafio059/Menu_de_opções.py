n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0
while op != 5:
    print('O que você deseja fazer com esses dois valores:')
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    op = int(input('----- Qual a sua opção? '))

    if op == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é: {}'.format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é: {}'.format(n1, n2, mult))
    elif op == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        elif n1 == n2:
            print('Os valores {} e {} são iguais'.format(n1, n2))
        else:
            print(f'Entre {n1} e {n2} o maior valor é {n2}') #testando f como format
    elif op == 4:
        print('INFORME DOIS NÚMEROS NOVAMENTE: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, digite novamente!')
print('Programa encerrado.')
