velocidade = int(input('Qual a velocidade atual do carro? '))
if velocidade < 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO, você excedeu o limite permitido que é de 80Km/h \n Você deve pagar uma multa de R${:.2f}!'.format((velocidade-80)*7))