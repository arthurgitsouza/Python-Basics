pessoas = {'nome': 'Arthur', 'idade': 18, 'sexo': 'M'}
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}') 