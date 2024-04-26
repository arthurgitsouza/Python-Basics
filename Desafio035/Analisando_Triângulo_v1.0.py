print('-=-'*20)
print('ANALIZANDO TRIÂNGULOSSS!!!!')
print('-=-'*20)
primeiro = float(input('Primeiro segmento: '))
segundo = float(input('Segundo segmento: '))
terceiro = float(input('Terceiro segmento: '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < segundo + primeiro:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRÂNGULO!')