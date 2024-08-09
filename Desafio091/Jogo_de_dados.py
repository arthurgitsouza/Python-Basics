from random import randint
from time import sleep
from operator import itemgetter
jogadas = {}
ranking = {}
print('Valores sorteados:')
for j in range(1,5): #Para cada jogada
    jogadas[f'jogada{j}'] = randint(1,6) #adicione uma chave para cada jogador e randomize um número para cada jogador
    print(f'jogador{j} tirou {jogadas[f"jogada{j}"]} no dado.')
    sleep(1)
    '''print(jogadas)''' #Para entender o print
print('-='*30)
print(f'{"RANKING DOS JOGADORES":=^30}')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True) #Esse comando ordena os valores da posição 1 do dicionário, no caso, os valores dos dados. 
#O reverse serve para colocar em ordem inversa!
#Devido a esse comando dessa biblioteca, ele vira uma lista e devo tratar ele como uma lista agora.
for i, v in enumerate(ranking):# i: indice de posição
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)