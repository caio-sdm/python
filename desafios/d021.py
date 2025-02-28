#programa que reproduza um arquivo mp3 (goddamn)

import pygame
pygame.init()
pygame.mixer.music.load('among.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
