resultado = {}
resultado['Nome'] = str(input('Nome: '))
resultado['Media'] = float(input(f'Média de {resultado['Nome']}: '))
if resultado['Media'] >= 7:
    resultado['Situação'] = 'Aprovado'
elif resultado['Media'] < 7 and resultado['Media'] >= 5:
    resultado['Situação'] = 'Recuperação'
else:
    resultado['Situação'] = 'Reprovado'
print('-='*40)
'''print(f'Nome é igual a {resultado["nome"]}')
print(f'Média é igual a {resultado["media"]}')
print(f'Situação é igual a {resultado["situação"]}')'''

#utilizando o for para esse print:
for k, v in resultado.items(): #Para cada keys e value na biblioteca resultados:
    print(f' - {k} é igual a {v}') #print a key e o valor para cada item dentro da biblioteca resultado.
print('-='*40)