def fatorial(num, show=False):
    f = 1 # Precisa começar com 1 pois se mutiplicar por 0 vai dar 0
    for i in range(num, 0, -1): #Contador de numero até 0 voltado 1
        if show :
            if i>1:
                print(f'{i} x ', end = '')
            else:
                print(f'{i} = ', end = '')
        f *= i # multiplicando todos os números
    return f
        


print(fatorial(5, show=True))