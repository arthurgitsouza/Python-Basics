palavras = ('APRENDER',
             'PROGRAMAR',
               'LNGUAGEM',
                 'PYTHON',
                   'CURSO',
                     'GRATIS',
                       'ESTUDAR',
                         'PRATICAR',
                           'TRABALHAR',
                             'MERCADO',
                               'PROGRAMADOR',
                                 'FUTURO')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end = '')
    for letras in p:
        if letras in 'AEIOU':
            print(letras, end = '')
#terminei tuplas até que fimmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm