lag = float(input('Largura da parede:'))
com = float(input('Comprimento da parede:'))

area = lag * com
litro = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(litro))
print('Sua parede tem dimensão de {}x{} e a sua área é de {}m²'.format(lag, com, area))