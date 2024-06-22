from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    ano_nascimento = int(input('Em que ano a {}ª pessoa nasceu?'.format(i)))
    if ano - ano_nascimento >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade!'.format(totmenor))
