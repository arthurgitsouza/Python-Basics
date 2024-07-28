from random import randint
numeros = (randint(0,6), randint(0,6), randint(0,6), randint(0,6), randint(0,6))
print(numeros)
em_ordem = sorted(numeros)
print(f'O maior número sorteado foi: {em_ordem[4]}')
print(f'O menor número sorteado foi: {em_ordem[0]}')
#outra forma:
print(f'O maior valor sorteado foi: {max(numeros)}') #O max funciona para tuplas
print(f'O menor valor sorteado foi: {min(numeros)}')