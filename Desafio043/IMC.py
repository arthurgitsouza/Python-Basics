peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso/(altura **2)
print('O IMC desta pessoa é de {}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso!')
elif imc == 18.5 and imc < 25:
    print('PARABÉNS, você está na faixa de peso NORMAL!')
elif imc == 25 and imc < 30:
    print('Você está na faixa de SOBREPESO!')
elif imc == 30 and imc < 40:
    print('Você está na faixa da OBESIDADE!')
else:
    cores = {'limpa' : '\033[m',
             'vermelho' : '\033[31m'}
    print('Você está na faixa da {}OBESIDADE MÓRBIDA{}, TOME CUIDADO!!!!!'.format(cores['vermelho'], cores['limpa']))