def contador(*num): #O 8 serve para dizer que não sei quantos parâmetros serão especificados.
    for valor in num:
        print(f'{valor} ', end = '')
    print('FIM!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)