# pygame é uma biblioteca de desenvolvimento de jogos para Python. 
# Ela fornece funcionalidades para criar jogos 2D, incluindo gráficos, sons e manipulação de eventos. 
# O código abaixo utiliza o pygame para tocar um arquivo de música chamado 'ex021pa.mp3'.
import pygame.mixer
pygame.init()
pygame.mixer.music.load('audio/ex021pa.mp3')
pygame.mixer.music.set_volume(0.2) #20% do volume
pygame.mixer.music.play()
#pygame.event.wait()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(60)
