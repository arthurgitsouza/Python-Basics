from random import randint #Random é uma biblioteca que serve para randomizar alguma escolha.
from time import sleep #Essa biblioteca mexe com o tempo e o sleep serve para deixar o computador dorminhoco pelos segundos colocados.
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. TENTE ADVINHAR!!!!')
print('-=-' * 20)
numero = int(input('Em que número inteiro eu pensei?? '))
n = randint(0,5) #O randint serve para escolher um número aleatorio inteiro. #Serve para o computador "pensar"
print('PROCESSANDO...')
sleep(3)
if numero == n:
    print('PARABÉNS, Você conseguiu me vencer')
else:
    print('GANHEII, Eu pensei no número {}, não no {}!'.format(n, numero))