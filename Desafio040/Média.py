n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))
if media >= 7.0:
    print('O aluno está APROVADO!')
elif media >= 5.0 and media < 7.0:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!')
    
'''
- Média abaixo de 5.0: REPROVADO

- Média entre 5.0 e 6.9: RECUPERAÇÃO

- Média 7.0 ou superior: APROVADO
'''