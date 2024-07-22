cont = soma = 0 # Quando colocado o True, não é necessário inicializar a variável n com 0!
while True:
    n = int(input('Digite um valor (999 para parar)'))
    if n == 999:
        break
    soma += n # Para relembrar: Serve para somas os números colocados no input!
    cont += 1
print(f'A soma dos {cont} valores foi {soma}')
    
