
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) #PEDRA É O 0, PAPEL É O 1, TESOURA É O 3, A VIRGULA SIGNIFICA "ENTRE"
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7;30m',
         'roxo' : '\033[35m',
         'vermelho' : '\033[31m',
         'verde' : '\033[32m'}
print('{}Suas opções:{} \n [0] PEDRA \n  [1] PAPEL \n   [2] TESOURA'.format(cores['amarelo'], cores['roxo']))
jogador = int(input('     Qual vai ser a sua jogada?? '))
print('{}JO'.format(cores['verde']))
sleep(1)
print('{}KEN'.format(cores['vermelho']))
sleep(1)
print('{}PO!!!!'.format(cores['amarelo']))
print('{}='.format(cores['azul'])*11)
print('Computador jogou {}!'.format(itens[computador]))
print('Jogador jogou {}!'.format(itens[jogador]))
print('='*11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('{}JOGADOR VENCEU!'.format(cores['verde']))
    elif jogador == 2:
        print('{}COMPUTADOR VENCEU!'.format(cores['vermelho']))
    elif jogador > 2:
        print('JOGADA INVALIDA!')
    else:
        print('Jogada invalida!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 1:
        print('{}EMPATE!')
    elif jogador == 2:
        print('{}JOGADOR VENCEU!'.format(cores['verde']))
    elif jogador == 0:
        print('{}COMPUTADOR VENCEU!'.format(cores['vermelho']))
    elif jogador > 2:
        print('JOGADA INVALIDA!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 2:
        print('{}EMPATE!')
    elif jogador == 0:
        print('{}JOGADOR VENCEU!'.format(cores['verde']))
    elif jogador == 1:
        print('{}COMPUTADOR VENCEU!'.format(cores['vermelho']))
    elif jogador > 2:
        print('JOGADA INVALIDA!')
    else:
        print('JOGADA INVÁLIDA!')
    #Jogo "JOKENPO" ou "Pedra, Papel, Tesoura" feito em python utilizando cadeia de condicionais com IF, ELIF e ELSE.
    