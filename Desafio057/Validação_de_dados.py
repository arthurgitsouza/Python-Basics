sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] #O zero não coloquei em meu codigo inicial, ele serve para levar em consideração apenas a primeira letra! Por exemnplo, caso o usuário tivesse escrito "Masculino" [0] serve para pegar apenas a primeira letra!
sexo_masculino = 'M'
sexo_feminino ='F'
while sexo != sexo_masculino and sexo != sexo_feminino:
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()
print('Sexo registrado com sucesso!!! ')
