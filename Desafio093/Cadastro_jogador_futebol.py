dados = {}
lista = []
tot = 0
cont_partidas = 0
dados['nome'] = str(input('Nome do jogador: '))
for p in range(0,5):
    gols = int(input(f'Quantos gols na partida {p}? '))
    cont_partidas += 1
    lista.append(gols)
    tot += gols 
    dados['gols'] = lista
    dados['total'] = tot
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados['nome']} jogou {cont_partidas} partidas.')
for pos in range(len(lista)):
    print(f'Na partida {pos}, fez {dados['gols'][pos]} gols.') # dados["gols"][pos] acessa o número de gols na partida pos da lista de gols armazenada em dados['gols'].