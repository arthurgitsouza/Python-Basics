n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
#verificando qual é o menor!
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3
#verificando qual é o maior"
if n1>n2 and n1>n3:
    maior = n1
if n2>n3 and n2>n1:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3
print('O menor valor digitado foi {}! \nO maior valor digitado foi {}!'.format(menor, maior))