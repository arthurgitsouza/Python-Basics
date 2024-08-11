total18 = 0
total_de_homens = 0
mulheres_menos_20 = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip()[0]
    while sexo not in 'MmFf':
        print('Informação inválida! Por favor, escreva novamente')
        sexo = str(input('Sexo: ')).strip()[0]
    if idade > 18:
        total18 += 1
    if sexo in 'Mm':
        total_de_homens += 1
    if sexo in 'Ff' and  idade < 20:
        mulheres_menos_20 += 1
    print('-'*20)
    op = str(input('Quer continuar? [S/N]')).strip()[0]
    if op in 'Nn':
        break
    while op not in 'SsNn':
        print('Informação inválida!')
        op = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-'*20)
print(f'Total de pessoas com mais de 18 anos: {total18}.')
print(f'Ao todo temos {total_de_homens} homens cadastrados.')
print(f'E temos {mulheres_menos_20} mulheres com menos de 20 anos.')


