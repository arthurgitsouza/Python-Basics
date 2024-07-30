expressao = str(input('Digite a expressão: '))
contd = conte = 0
if '(' in expressao:
    contd += 1
elif ')' in expressao:
    conte += 1
else:
    print('Não há parenteses nessa expressão')
if contd == conte:
    print('Expressão Válida!')
else:
    print('Expressão inválida!')