print('-=-'*20)
print('ANALIZANDO TRIÂNGULOSSS!!!!')
print('-=-'*20)
primeiro = int(input('Primeiro segmento: '))
segundo = int(input('Segundo segmento: '))
terceiro = int(input('Terceiro segmento: '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < segundo + primeiro: #SERVE PARA QUE O FIM DA LINHA NÃO SEJA NADA!
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!', end='')
    if primeiro == segundo and segundo == terceiro:
        print('EQUILÁTERO!')
    elif primeiro != segundo and segundo != terceiro and primeiro != terceiro:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRÂNGULO!')