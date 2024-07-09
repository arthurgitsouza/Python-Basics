pergunta = 'S'
soma = cont = media = 0
while pergunta in 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1 
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    media = soma/cont
print(f'Você digitou {cont} números e a média entre eles é: {media:.2f}')