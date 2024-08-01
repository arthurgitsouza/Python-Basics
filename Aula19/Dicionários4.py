Brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla' : 'SP'}
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil) #Criou uma lista com dois dicionários dentro da lista
print(Brasil[0])#Pegou o dicionário que a lista continha no valor 0
print(Brasil[1])#Pegou o dicionário que a lista continha no valor 1
print(Brasil[1]['uf'])