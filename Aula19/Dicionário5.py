estado = {}
brasil = []
for c in range(0, 3): #A cada 3 vzs, faça isso aq
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil: #Para cada dicionário de estado na lista brasil:
    print(e)
print('-'*30)
for e in brasil: #Para cada dicionário de estado na lista brasil:
    for k, v in e.items(): #Para cada chave e valores em itens de e (que foram os estados colocados)
        print(f'O campo {k} tem valor {v}')
        print(v, end = '')