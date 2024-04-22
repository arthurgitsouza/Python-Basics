frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('A primeira letra A apareceu pela primeira vez na posição {}'.format(frase[0::].find('A')+1))
print('A ultima letra A apareceu pela primeira vez na posição {}'.format(frase.rfind('A')+1))