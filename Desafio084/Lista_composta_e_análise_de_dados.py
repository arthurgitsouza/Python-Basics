dados = []
pessoas_cadastradas = []
max_peso = min_peso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    op = str(input('Quer continuar? ')).strip()[0]
    if len(pessoas_cadastradas) == 0: #Se ainda não foi cadastrado ninguém
        max_peso = min_peso = dados[1] #O maior e o menor, vai ser o dado do primeiro input
    else:
        if dados[1] > max_peso:
            max_peso = dados[1]
        if dados[1] < min_peso:
            min_peso = dados[1]
    pessoas_cadastradas.append(dados[:])
    dados.clear()
    while op not in 'SsNn':
        print('Opção inválida! Tente novamente entre [S] ou [N]!')
        op = str(input('Quer continuar? ')).strip()[0]
    if op in 'Nn':
        break
print('-'*30)
print(f'Ao todo, você cadastrou {len(pessoas_cadastradas)} pessoas.')
print(f'O maior peso foi de {max_peso}. O peso de ')
for p in pessoas_cadastradas:
    if p[1] == max_peso:
        print(f'{p[0]}')
print(f'O menor peso foi de {min_peso}. O peso de ')
for p in pessoas_cadastradas:
    if p[1] == min_peso:
        print(f'{p[0]}', )

    
        