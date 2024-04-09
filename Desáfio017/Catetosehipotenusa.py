from math import hypot
catetooposto = float(input('Comprimento do cateto oposto: '))
catetoadjacente = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir: {:.2f}'.format(hypot(catetooposto, catetoadjacente)))
