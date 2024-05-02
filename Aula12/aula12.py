nome = str(input('Qual o seu nome: '))
if nome == 'Arthur':
    print('Que nome bonito!')
elif nome == 'Mackley' or nome == 'Dominick' or nome == 'Janete':
    print('Seu nome é bem maneiro!!')
elif nome in 'Ana Cláudia Mariana Heloise Joana Lucia Amanda Carolina Caroline Luana Thainara':
    print('Que belo nome feminino você tem, parabéns!')
else:
    print('Seu nome é bem normal!')
print('Tenha um ótimo dia, {}!'.format(nome))