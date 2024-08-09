from time import sleep

def contagem(i, f, p): # i = inicio, f = fim, p = passos
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p == 0:
        p = 1
    if i > f:
        for cont in range(i, f-1, -p): # O '-' no p serve para que os passos sejam feitos em forma negativa, ou seja, de trás para frente
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
    else:
        for cont in range(i, f+1, p): # O +1 e o -1 é para acrescentar o ultimo número que o py nn conta
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
    print('FIM!')
    print('-=' * 20)

contagem(i=1, f=10, p=1)
contagem(i=10, f=0, p=2)

print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('-=' * 20)
contagem(i, f, p)
