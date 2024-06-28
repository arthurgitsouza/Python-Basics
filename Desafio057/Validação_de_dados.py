sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
sexo_masculino = 'M'
sexo_feminino ='F'
while sexo != sexo_masculino and sexo != sexo_feminino:
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:'))