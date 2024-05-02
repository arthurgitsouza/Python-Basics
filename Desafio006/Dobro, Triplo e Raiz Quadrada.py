n1 = int(input('Qual o seu número?'))
s = n1 * 2
s2 = n1 * 3
s3 = n1 ** (1/2)
print('O seu dobro é {}, o seu triplo é {}'.format(s, s2), end=' ')
print('e a sua raiz quadrada é {:.2f}'.format(s3))

# De forma mais simples o código:
# n1 = int(input('Qual o seu número?'))
# print('O seu dobro é {}, o seu triplo é {}'.format(n1*2, n1*3), end=' ')
# print('e a sua raiz quadrada é {:.2f}'.format(n1**1/2))