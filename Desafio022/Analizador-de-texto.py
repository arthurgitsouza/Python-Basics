import pygame
import emoji
from time import sleep
pygame.init()
nome = input('Digite seu nome completo: ').strip()
print(emoji.emojize('\n:barco_a_vela: Analizando seu nome, tenha calma:lancha:...', language="pt"))
sleep(2)
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) -nome.count(' ')))
divisao = nome.split()
nome1 = divisao[0]
nome2 = divisao[1]
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome1, len(nome1)))
print('Seu segundo nome é {} e ele tem {} letras'.format(nome2, len(nome2)))
print(emoji.emojize(':red_heart: E o seu nome é muito bonito, assim como você:red_heart:'))
print('\n\nFique com essa música>>>>>>>>')
pygame.mixer.music.load('misterio.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
