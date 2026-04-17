
from pygame.locals import *  # noqa: F403
import pygame
import sys

pygame.init()

DISPLAYSURF=pygame.display.set_mode((800,600))
pygame.display.set_caption("Hello World!")
while True: #principal loop
    for event in pygame.event.get():
        if event.type==QUIT:  # noqa: F405
            pygame.quit()
            sys.exit()
        pygame.display.update()