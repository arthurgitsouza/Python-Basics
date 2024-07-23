número_jogadores = int(input('Quantos jogadores se inscreveram no jogo: '))
soma = 0
for j in range(1, número_jogadores+1):
    players = int(input(f'Jogador n°{j}, selecione um número de 0 a 100: '))
    soma += players
    média = soma/número_jogadores
print(média)




















'''from time import sleep
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7;30m',
         'roxo' : '\033[35m',
         'vermelho' : '\033[31m',
         'verde' : '\033[32m'}
print(f'{cores['amarelo']}{'='*40}{cores['limpa']}')
sleep(2)
print(f'{cores['vermelho']}{'BEM VINDO':^40}{cores['limpa']}')
sleep(2)
print(f'{cores['vermelho']}{'AO':^40}{cores['limpa']}')
sleep(2)
print(f'{cores['amarelo']}{'='*40}{cores['limpa']}')
print(f'{cores['vermelho']}{'JOGO DO REI DE OUROS':-^40}{cores['limpa']}')
print(f'{cores['amarelo']}{'='*40}{cores['limpa']}')'''
