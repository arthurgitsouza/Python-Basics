dados = {}
cadastros = []
total = 0
lista_mulheres = []
acima_da_media = []
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while dados['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    dados['idade'] = int(input('Idade: '))
    cadastros.append(dados.copy())
    dados.clear()
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while op not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op in 'Nn':
        break
for i, pessoa in enumerate(cadastros): #Para cada i [dicionario presente na lista] acesse pessoas [cada dicionário que contem sexo, nome e idade] 
    total += pessoa['idade'] #O total vai ser a soma da idade de cada pessoa presente na lista, a pessoa é o dicionário acessado pelo range
    media = total / len(cadastros)
print(cadastros)
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas!')
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) Lista das pessoas que estão acima da média:')
for i, pessoa in enumerate(cadastros):
    if pessoa['sexo'] in 'F':
        lista_mulheres.append(pessoa['nome'])
    if media < pessoa['idade']+1:
        acima_da_media.append(pessoa)
    print(f'nome = {pessoa["nome"]}; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]};')
print(f'D) As mulheres cadastradas foram {lista_mulheres}' )
print('FINALIZADO')
