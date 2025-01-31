import pygame
import constants

class Personaje():
    def __init__(self,x,y):
        self.shape = pygame.Rect(0,0,constants.ANCHO_PERSONAJE,constants.ALTO_PERSONAJE)
        self.shape.center = (x,y)

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz,(constants.COLOR_PERSONAJE),self.shape)