from time import sleep
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
print(f'{cores['amarelo']}{'='*40}{cores['limpa']}')

número_jogadores = int(input('Quantos jogadores se inscreveram no jogo: '))
soma = 0
cont1 = 0
jogadas = []

for j in range(1, número_jogadores+1):
    while True:
        try:
            players = int(input(f'Jogador n°{j}, selecione um número de 0 a 100: '))
            if 0 <= players <= 100:
                jogadas.append(players)
                soma += players
                break
            else:
                print('Por favor, selecione um número entre 0 e 100.')
        except ValueError:
            print('Entrada inválida. Por favor, selecione um número entre 0 e 100.')
média = soma / número_jogadores
resultado_final = média * 0,8

menor_diferença = None
vencedor = None

for jogada in jogadas:
    diferença = abs(jogada - resultado_final)
    
    if menor_diferença is None or diferença < menor_diferença:
        menor_diferença = diferença
        vencedor = jogada
print(f'{cores['amarelo']}{'Vamos ver os números escolhidos...'}{cores['limpa']}')
sleep(2)
print(f'{cores['amarelo']}{'Calculando...'}{cores['limpa']}')
sleep(3)
print(f'o valor médio dos números escolhidos na rodada foi:  {média}')
print('Após multiplicar esse valor por 0,8...')
print(f'O resultado final (média * 0.8) é: {resultado_final}')
print(f'O vencedor é o jogador que escolheu o número mais próximo de {resultado_final}, que foi: {vencedor}')




















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
