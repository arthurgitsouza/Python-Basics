contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n >= 0 and n <= 20:
        print(f'Você digitou o número {contagem[n]}!') #Aqui ele usa o N para procura em 'contagem' o número que refere a variável que está dentro da tupla, tipo assim, o número 20 ele vai procurar exatamente a vigezima variável.
        op = str(input('Você quer continuar? [S/N]')).strip()[0]
        if op in 'Ss':
            n = int(input('Digite um número entre 0 e 20: '))
        else:
            break
    else:
        print('Tente novamente. Digite um número entre 0 e 20: ')
        n = int(input('Digite um número entre 0 e 20: '))
#FAZER UM QUESTIONAMENTO SE O USUÁRIO VAI QUERER CONTINUAR OU NÃO!