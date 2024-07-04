import pygame
pygame.mixer.init()

somaidade = 0
maisvelho = 0
maisvelho_nome = ''
totmulher = 0

for pess in range(1, 5):
    print('--------{}ª PESSOA--------'.format(pess))
    n = str(input('Nome: ')).strip().capitalize()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()  
    somaidade += i
    
    if pess == 1 and s == 'M':
        maisvelho = i
        maisvelho_nome = n
    if s == 'M' and i > maisvelho:
        maisvelho = i
        maisvelho_nome = n
    if s == 'F' and i < 20:
        totmulher += 1      

media1 = somaidade / 4

print('A média de idade do grupo é de {} anos!'.format(media1))
print('O homem mais velho tem {} anos e se chama {}'.format(maisvelho, maisvelho_nome))
print('Existem {} mulheres com idade inferior a 20 anos na lista!'.format(totmulher))

pygame.mixer.music.load('ele-fezz-de-novo-incansavel.mp3')  
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
