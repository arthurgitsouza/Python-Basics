# Escopo Global:
def teste():
    x = 8
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste x vale {x}')


# Programa Principal:
n = 2
print(f'No programa principal, n vale {n}.')
teste()
print(f'Na função teste, x vale {x}')
# Isso se chama escopo Global, pois a variável N por ser inicializada fora da função, ela pode rodar fora da função também


