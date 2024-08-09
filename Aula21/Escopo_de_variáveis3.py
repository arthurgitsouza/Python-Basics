def teste (b):
    global a # Não crie uma variável a, use o a global. # Ele apaga o 5 e faz o 5 valer 8
    a = 8
    b += 4 # O b que antes recebia o a de fora recebe o a de dentro
    c = 2
    print(f'"A" dentro vale {a}')
    print(f'"B" dentro vale {b}')
    print(f'"C" dentro vale {c}')
    
    
a = 5
teste(a)
print(f'"A" fora vale {a}')

