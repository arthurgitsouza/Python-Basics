frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'''Com isso primeiro eu separei a frase em palavras'''
'''Após isso, juntei com o "join" as palavras  fazendo com que elas perdessem o espaço no comando ''.'''
inverso = ''
for letra in range(len(junto) -1, - 1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo')

    '''Não entendi nada!!!!! Depois voltar pra ver a aula 053!'''
    '''Nessa aqui só copiei o exercicio!'''