def contador(i, f, p):
    """
    -> Faz uma contagem e mostra  na tela!
    parametros/args:
        i : início da contagem
        f : fim da contagem
        p : passo da contagem
        return : sem retorno
    FUNÇÃO CRIADA DURANTE A AULA DE FUNÇÕES
    """
    c = i
    while c <= f:
        print(f'{c} ', end = '')
    print('FIM!')
    
    
help(contador)