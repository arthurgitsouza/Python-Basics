nome = str(input('Escreva o seu nome completo: ')).strip()
print('Prazer em te conhecer {}'.format(nome))
nome_separado = nome.split()
print('Seu primeiro nome é {}.'.format(nome_separado[0]))
print('Seu último nome é {}.'.format(nome_separado[-1]))
#O -1 serve para ler de trás para frente.