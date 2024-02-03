import pygame
pygame.init()
pygame.mixer.music.load('soundscrate-thunder.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
pygame.quit()