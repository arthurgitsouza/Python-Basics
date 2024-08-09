a = (5, 5, 5, 5)
b = (8, 8, 8, 8)
c = a + b
d = b + a
print(c)
print(d)
print(len(c))
print(len(d))
print(c.count(5)) #Conta quantas vezes aparece esse valor
print(c.count(9)) #Conta quantas vezes aparece esse valor
print(c.index(8)) #Essa função é utilizada para saber a posição do valor
print(d.index(5, 1)) #Serve para achar o 2° valor na posição, o primeiro 5 da tupla D aparece no 0, enquanto o segundo vai ser mostrado no print na posição 5.
