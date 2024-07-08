pergunta = n = cont = soma = 0
while pergunta != 'S' or 'N':
    n = int(input('Digite um número: '))
    pergunta = str(input('Quer continuar: [S/N]')).upper().strip()
    soma += n
    cont =+ 1
    media = (soma/cont)
print(f'Você digitou {cont} números e a media foi {soma}.')