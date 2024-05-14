nome = 'Arthur'
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7;30m',
         'roxo' : '\033[35m',
         'vermelho' : '\033[31m',
         'verde' : '\033[32m'}
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['verde'], nome, cores['limpa']))