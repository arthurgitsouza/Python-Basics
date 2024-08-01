pessoas = {'nome': 'Arthur', 'idade': 18, 'sexo': 'M'}
for k in pessoas.keys(): #Para cada kays no dicionário pessoa
    print(k) #print as keys
print('-'*40)
for k in pessoas.values():
    print(k)
print('-'*40)
for k, v in pessoas.items():
    print(f'{k} = {v}') 