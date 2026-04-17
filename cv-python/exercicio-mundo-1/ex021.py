# pygame é uma biblioteca de desenvolvimento de jogos para Python. 
# Ela fornece funcionalidades para criar jogos 2D, incluindo gráficos, sons e manipulação de eventos. 
# O código abaixo utiliza o pygame para tocar um arquivo de música chamado 'ex021pa.mp3'.
import pygame 
pygame.init()
pygame.mixer.music.load('ex021pa.mp3')
pygame.mixer.music.play()
pygame.event.wait()
