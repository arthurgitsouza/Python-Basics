distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km!'.format(distancia))
perto = distancia*0.50
longe = distancia*0.45
if distancia <= 200:
    print('E o preço de sua viagem será de R${:.2f}!'.format(perto))
else:
    print('E o preço de sua viagem será de R${:.2f}!'.format(longe))