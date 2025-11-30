import pygame
import planetclass
from math import cos, sin
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Simulador de orbitas:")

p1 = planetclass.planet(200, 400,(0,255,0), 40, 300, 300, 400)
teta = 0
#para que no se cierre:
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    p1.x = p1.xrot + p1.ratiorot * cos(teta)
    p1.y = p1.yrot + p1.ratiorot * sin(teta)
    teta += 0.01
    pygame.draw.circle(screen, (0, 180, 0), (p1.x, p1.y), p1.ratio)
    pygame.display.flip()

pygame.quit()



