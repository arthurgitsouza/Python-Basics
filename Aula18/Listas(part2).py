teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 42
galera.append(teste[:])
'''galera.append(teste)''' #Se for escrito assim, sem fazer uma cópia, vai ser alterado nos dois valores.
print(galera)