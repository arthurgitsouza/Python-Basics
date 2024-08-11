from time import sleep
from random import randint
conttentativas = 0
print('Sou seu computador...')
sleep(2)
print('\nE eu acabei de pensar em um número entre 0 e 10!!!')
sleep(3)
print('\nSerá que você consegue advinhar qual foi?')
numero_sorteado = randint(0, 10)
#print(numero_sorteado)
num = int(input('Qual é o seu palpite?? '))
while num != numero_sorteado:
    conttentativas += 1
    if num < numero_sorteado:
        print('Mais.. Tente mais uma vez.')
        num = int(input('Qual é o seu novo palpite? '))
    else:
        print('Menos... Tente mais uma vez.')
        num = int(input('Qual é o seu novo palpite? '))
print('Parabéns, você acertou, o número que eu pensei realmente era o {}, você acertou com um total de {} tentativas'.format(numero_sorteado, conttentativas + 1))