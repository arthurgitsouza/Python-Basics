from time import sleep

def maior(* numeros): # Criação de uma função com nome 'Maior' e que recebe números em uma quantidade indefinida.
    cont = maior = 0 # O contador e o maior número iniciam com 0
    print('\nAnalisando os valores passados...')
    for n in numeros: # Para cada número nos números:
        print(f'{n} ', end = '', flush=True)
        sleep(0.3)
        if cont == 0: # O cont serve para saber em qual número está, como uma posição, nesse caso se não tiver nenhum número analisado ainda, então:
            maior = n # Então o maior número será esse!
        else: # Senão
            if n > maior: # Se o número for maior que o maior número
                maior = n # O maior vai ser esse número.
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()