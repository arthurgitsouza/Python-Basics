from datetime import date
ano_de_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento
print('O atleta tem {} anos!'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <=14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <=19:
    print('Classificação: JÚNIOR')
elif idade > 19 and idade <=25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

'''
Até 9 anos: MIRIM

- Até 14 anos: INFANTIL

- Até 19 anos: JÚNIOR

- Até 25 anos: SÊNIOR

- Acima de 25 anos: MASTER
'''