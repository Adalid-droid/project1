import pygame
import const
import personaje
from personaje import Personaje
jugador = Personaje(50,50)

pygame.init()
ventana = pygame.display.set_mode((const.ANCHO_VENTANA,const.ALTO_VENTANA))
run = True
pygame.display.set_caption("mi primero juego")
#definir el estado de la tecla
mover_arriba = False
mover_abajo = False
mover_izquieda = False
mover_derecha = False
#colocar el frame rate
reloj = pygame.time.Clock()
while run: 
    #que vaya 60 fps
    reloj.tick(const.FPS)

    ventana.fill(const.COLOR_BG)
    #calcular el movimiento del jugasdwador
    delta_x = 0
    delta_y = 0
    if mover_derecha == True:
        delta_x = const.VELOCIDAD
    if mover_izquieda == True:
        delta_x = -const.VELOCIDAD
    if mover_arriba == True:
        delta_y = -const.VELOCIDAD
    if mover_abajo == True:
        delta_y = const.VELOCIDAD
    #mover al jugador
    jugador.movimiento(delta_x,delta_y)
    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type== pygame.KEYDOWN:
            if event.key ==  pygame.K_a:
                mover_izquieda = True
            if event.key ==  pygame.K_d:
                mover_derecha = True
            if event.key ==  pygame.K_w:
                mover_arriba = True
            if event.key ==  pygame.K_s:
                mover_abajo = True
        if event.type == pygame.KEYUP:
            if event.key ==  pygame.K_a:
                mover_izquieda = False
            if event.key ==  pygame.K_d:
                mover_derecha = False
            if event.key ==  pygame.K_w:
                mover_arriba = False
            if event.key ==  pygame.K_s:
                mover_abajo = False            

    pygame.display.update()
pygame.quit()
