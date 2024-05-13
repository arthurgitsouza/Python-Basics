num = int(input('Digite um número inteiro: '))
cores = {'limpa' : '\033[m', 
         'roxo' : '\033[34m',
         'vermelho' : '\033[31m',
         'rosa'  : '\033[35m'}
print('{}Escolha uma dessas opções: {}\n[1] converter para BINÁRIO \n[2] converter para OCTAL \n[3] converter para HEXADECIMAL{}'.format(cores['vermelho'],cores['roxo'], cores['limpa']))
op = int(input('{}Sua opção:'.format(cores['rosa'])))