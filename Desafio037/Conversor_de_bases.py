num = int(input('Digite um número inteiro: '))
cores = {'limpa' : '\033[m', 
         'roxo' : '\033[34m',
         'vermelho' : '\033[31m',
         'rosa'  : '\033[35m'}
print('{}Escolha uma dessas opções: {}\n[1] converter para BINÁRIO \n[2] converter para OCTAL \n[3] converter para HEXADECIMAL{}'.format(cores['vermelho'],cores['roxo'], cores['limpa']))
op = int(input('{}Sua opção:{}'.format(cores['rosa'], cores['limpa'])))
if op == 1:
    print('O número {} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!') 