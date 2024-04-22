cidade = input('Em que cidade você nasceu? ').strip()
print(cidade[:5].upper() == 'SANTO')

#O cidade[:5] serve para analisar os 4 primeiros caracteres da string,
#o upper vai transformar toda a sentença em maiúsculo, para não ter erro na verificação de 'SANTO'
