# Escopo Global:
def teste():
    x = 8
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste x vale {x}')


# Programa Principal:
n = 2
print(f'No programa principal, n vale {n}.')
# Isso se chama escopo Global, pois a variável N por ser inicializada fora da função, ela pode rodar fora da função também
teste()
# print(f'Na função teste, x vale {x}')
# Diferente daqui, que se chama Escopo Local, pois a variável foi inicializada dentro da função e não funciona no programa principal

