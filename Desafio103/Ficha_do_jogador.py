def ficha(nome='', gols=''):
    if gols.isnumeric():
        gol = int(gols)
    else:
        gols = 0
    if nome == '':
        print(f'O jogador <desconhecido> fez {gols} gol(s).')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
num = int(input('Número de gols: '))
ficha(n, num)
