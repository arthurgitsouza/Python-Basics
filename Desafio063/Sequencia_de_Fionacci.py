print('-'*23)
print('Sequencia de Fibonacci!')
print('-'*23)
termos = int(input('Quantos termos você quer mostrar? '))
print('~'*30)
termoum = 0
termodois = 1
print(f'{termoum} > {termodois}', end = '')
cont = 3
while cont <= termos:
    termotres = termoum + termodois
    print(f'> {termotres}', end = '')
    termoum = termodois
    termodois = termotres
    cont += 1
print(' > FIM')
print('~'*30)
