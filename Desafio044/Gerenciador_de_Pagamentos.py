cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7;30m',
         'roxo' : '\033[35m',
         'vermelho' : '\033[31m',
         'verde' : '\033[32m'}
print('{}={}'.format(cores['azul'], cores['limpa'])*20, end=(''))
print(' {}LOJAS DO ARTHUR{} '.format(cores['amarelo'], cores['limpa']), end=(''))
print('{}='.format(cores['azul'])*20)
preço = float(input('Preço das compras: R$'))
print('='*20)
print('{}FORMAS DE PAGAMENTO:'.format(cores['amarelo']))
print('{}[1] à vista dinheiro/cheque \n[2] à vista cartão \n[3] 2x no cartão \n[4] 3x ou mais no cartão'.format(cores['azul']))
op = int(input('Qual a sua opção? '))
if op == 1:
    calculo = preço - (10/100 * preço)
    print('{}Sua compra de {:.2f}R$ vai custar {:.2f}R$ no final!'.format(cores['amarelo'], preço, calculo))
elif op == 2:
    calculo = preço - (5/100 * preço)
    print('{}Sua compra de {:.2f}R$ vai custar {:.2f}R$ no final!'.format(cores['amarelo'], preço, calculo))
elif op == 3:
    print('{}Sua compra custará {}'.format(cores['amarelo'], preço))
elif op == 4:
    calculo = preço + (20/100 * preço)
    parcelas = int(input('Quantas parcelas? '))
    parcela = calculo / parcelas
    print('{}Sua compra será parcelada em {}x de R${:.2f} COM JUROS{}'.format(cores['amarelo'], parcelas, parcela, cores['limpa']))
    print('{}Sua compra de {:.2f}R$ vai custar {:.2f}R$ no final!'.format(cores['amarelo'], preço, calculo))
else:
    print('{}ERROR, a opção digitada não é válida!\n{}         Tente novamente!'.format(cores['vermelho'], cores['amarelo']))

