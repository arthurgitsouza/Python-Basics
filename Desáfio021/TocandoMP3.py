import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.250)
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)