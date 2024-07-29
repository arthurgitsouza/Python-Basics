valores = []

for c in range(5):
    n = int(input('Digite um valor: '))

    if c == 0 or n > valores[-1]:  # Se for o primeiro valor ou se o número for maior que o último número da lista
        valores.append(n)  # Adiciona esse valor no final da lista
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)  # Insere o valor na posição correta
                print(f'Adicionado na posição {pos} da lista!')
                break
            pos += 1  # Incrementa a posição para continuar a verificação

print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
