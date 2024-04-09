a = input('digite qualquer coisa:')
print('O tipo primitivo do valor é: {}'.format(type(a)))
print('O termo digitado,{},só tem espaços?'.format(a), a.isspace())
print('{} É numerico?'.format(a), a.isnumeric())
print('{} É alfabetico?'.format(a), a.isalpha())
print('{} É alfanumerico?'.format(a), a.isalnum())
print('{} Está em letras maiúsculas?'.format(a), a.isupper())
print('{} Está em letras minusculas?'.format(a), a.islower())
print('{} Está capitalizada?'.format(a), a.istitle())

#Testando os valores colocados no input!