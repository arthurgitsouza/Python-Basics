lista = []
lista_pares = []
lista_impares = []
for v in range(5): #O v é o indice, não o valor colocado pelo usuário!!!! #A posição
    lista.append(int(input('Digite um número: ')))
    if lista[v] % 2 == 0: #Já o lista[v] retoma o input feito pelo usuário!
        lista_pares.append(lista[v])
    else:
        lista_impares.append(lista[v])
print('-='*30)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_impares}')