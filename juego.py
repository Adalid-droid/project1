import pygame
import constants
import personaje
from personaje import Personaje
jugador = Personaje(50,50)

pygame.init()
ventana = pygame.display.set_mode((constants.ANCHO_VENTANA,constants.ALTO_VENTANA))
run = True
pygame.display.set_caption("mi primero juego")
while run:

    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    pygame.display.update()
pygame.quit()