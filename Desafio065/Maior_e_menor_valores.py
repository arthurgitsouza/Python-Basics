pergunta = 'S'
soma = cont = media = menor = maior = 0
while pergunta == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1 
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média entre eles é: {media:.1f}!')
print(f'O maior valor foi{maior} e o menor valor foi {menor}!')