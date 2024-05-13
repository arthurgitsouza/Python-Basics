valor = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
parcelamento = valor / (anos * 12)
minimo = salario - (30/100 * salario)
print('Para pagar uma casa de {:.2f} em {} anos'.format(valor, anos))
print('A prestação será de R${:.2f}'.format(parcelamento))
if parcelamento <= minimo:
    print('Empréstimo ACEITO!')
else:
    print('Empréstimo NEGADO!')
    
    
    
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.