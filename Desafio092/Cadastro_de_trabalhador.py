ctps = {}
ano_atual = 2018
ctps['nome'] = str(input('Nome: '))
an = int(input('Ano de Nascimento: '))
ctps['idade'] = ano_atual - an
ctps['carteira'] = int(input('Carteira de Trabalho: (0 não tem): '))
if ctps['carteira'] != 0:
        ctps['contratação'] = int(input('Ano de Contratação: '))
        ctps['salário'] = float(input('Salário: R$'))
        ctps['aposentadoria'] = (2015 + 35) - an  #O ano para aposentadoria é  a soma do ano que ela começou a trabalhar + a quantidade de tempo de trabalho menos o ano de nascimento.
print('-='*30)
for k, v in ctps.items():
        print(f'   - {k} tem o valor de {v}')

    
#67