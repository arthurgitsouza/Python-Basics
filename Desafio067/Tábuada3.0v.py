while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print('-'*20)
    for i in range(1,11):
        mult = valor * i
        print(f'{valor} x {i} = {mult}')
    print('-'*20)
print('PROGRAMA TABUADA ENCERRADO POIS O NÚMERO É NEGATIVO! \nvolte sempre.')