time = []
jogador = {}
partidas = []
tot = 0

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for p in range(tot):
        partidas.append(int(input(f'Quantos gols na partida {p}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    
    while True:
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if op in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    
    if op == 'N':
        break

print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-=' * 30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-=' * 30)
