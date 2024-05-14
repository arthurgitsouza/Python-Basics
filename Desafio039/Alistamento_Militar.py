from datetime import date
ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print('Quem nasceu em {} tem {} anos em 2024.'.format(ano, idade))
alistamento_menos_de_18 = 18 - idade
alistamento_mais_de_18 = idade - 18
ano_do_alistamento = ano_atual + alistamento_menos_de_18 
ano_do_alistamento2 = ano_atual - alistamento_mais_de_18
if idade < 18:
    print('Ainda faltam {} anos para o alistamento!'.format(alistamento_menos_de_18))
    print('Seu alistamento será em {}'.format(ano_do_alistamento))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos'.format(alistamento_mais_de_18))
    print('Seu alistamento foi em {}'.format(ano_do_alistamento2))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
 
'''ano = int(input('Ano de nascimento: '))
ano_atual = 2024
idade = ano_atual - ano
print('Quem nasceu em {} tem {} anos em 2024.'.format(ano, idade))
alistamento_menos_de_18 = 18 - idade
alistamento_mais_de_18 = idade - 18
ano_do_alistamento = ano_atual + alistamento_menos_de_18 
ano_do_alistamento2 = ano_atual - alistamento_mais_de_18
if idade < 18:
    print('Ainda faltam {} anos para o alistamento!'.format(alistamento_menos_de_18))
    ano_do_alistamento = ano_atual + alistamento_menos_de_18
    print('Seu alistamento será em {}'.format(ano_do_alistamento))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos'.format(alistamento_mais_de_18))
    ano_do_alistamento = ano_atual - alistamento_mais_de_18
    print('Seu alistamento foi em {}'.format(ano_do_alistamento2))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
    
    
    
Dessa forma, o calculo só seria realizado caso a condição fosse realizada! Bem mais prático!'''