dados = []
lista = []
medias = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    media = (dados[1] + dados[2]) / 2
    medias.append(media)
    lista.append(dados[:])
    dados.clear()
    op = str(input('Quer continuar? [S/N] ')).strip()[0]
    while op not in 'SsNn':
        print('Opção inválida, escreva novamente!')
        op = str(input('Quer continuar? [S/N]'))
    if op in 'Nn':
        break
print('-='*40)
print(f'{"no.":<4} {"NOME":<10} {"MÉDIA":<5}')
print('-'*30)
for pos in range(len(lista)): #Para cada posição no tamanho total da lista
        print(f'{pos:<4} {lista[pos][0]:<10} {medias[pos]:<5.2f}')
while True:
    op = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if op == 999:
        break
    if 0 <= op < len(lista):  # Verifica se o índice é válido
        print(f'As notas de {lista[op][0]} são {lista[op][1]} e {lista[op][2]}')
    else:
        print('Índice inválido.')
    