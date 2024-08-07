from random import randint
números = []

def sorteia():
    print('Sorteando 5 valores da lista: ', end = '')
    for num in range(5):
        números.append(randint(1,10))
    print(f'{números} PRONTO!')


def somaPar(lista):
    soma = 0
    for número in lista:
        if número % 2 == 0:
            soma += número
    print(f'Somando os valores pares de {lista}, temos {soma}.')
    
sorteia()
somaPar(números) # O parâmetro 'lista' receberá a lista 'números'