lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim' # numerado como 0, 1, 2, 3
# Tuplas são imutáveis
#lanche[1] = 'Refrigerante' == error
print(lanche)
print(lanche[1])
print(lanche[2])
print(lanche[0])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
lanche[1] = 'Refrigerante'
print(lanche[1])