salario = float(input('Qual é o sálario do funcionário? R$'))
reajuste = salario + (salario*15/100)
print('Um funcionário que ganhava {:.2f}, com desconto de 15%, passa a receber R${:.2f}'.format(salario, reajuste))