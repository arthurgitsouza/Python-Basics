salario = float(input('Qual é o sálario do funcionario: '))
if salario <= 1250:
   salario1 = salario + (15/100 * salario)
if salario > 1250:
    salario1 = salario + (10/100 * salario)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora!'.format(salario, salario1))