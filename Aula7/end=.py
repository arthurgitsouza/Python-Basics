n1 = int(input('Qual o valor?'))
n2 = int(input('Qual o outro valor?'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma desses números é {}, a mutiplicação é {}, a divisão é {:.1f}, a divisão inteira é {} e o resultado da potência é {}'.format(s, m, d, di, e), end=' ')
print('teste para colagem com o end=''')

# O end='' serve para colopcar o output na mesma linha, ou seja, será printado na mesma linha.
# O n/ serve para quebrar a linha do output.