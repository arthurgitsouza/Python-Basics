from random import randint
print('-'*30)
print('VAMOS JOGAR PAR OU IMPAR!')
print('-'*30)
computador = randint(0,10)
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    decisao = str(input('Par ou Impar? [P/I]')).strip().upper()
    total = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}!')
    if decisao == 'P' and total % 2 == 0:
        print('E {total} é Par, então...')
        print('Você VENCEU!! \nMas... Vamos jogar novamente...')
        cont +=1
    else:
        print(f'{total} é impar, então...')
        print('Você PERDEU!')
        print(f'GAME OVER! e Você venceu apenas {cont} vezes.')
        break