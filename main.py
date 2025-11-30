import pygame
import planetclass
from math import cos, sin
pygame.init()

#const:
G = 6.67430e-11
escala = 1e11
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Simulador de orbitas:")

p1 = planetclass.planet(200, 300,(0,255,0), 40, 2e30, 0, 0)
p2 = planetclass.planet(200, 200, (255,0,0),10, 6e24,3500*escala ,0)
#escala
body = [p1,p2]
forces = [0, 0]
forcesx = 0
forcesy = 0
dt = 0.00001
#para que no se cierre:
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    for w in range(len(forces)):
        forces[w] = 0
    for i in range(len(body)):
        forcesx = 0
        forcesy = 0
        for j in range(len(body)):
            if i!=j:
                dx = (body[j].x-body[i].x)
                dy = (body[j].y-body[i].y)
                norm = (dx)**2+(dy)**2
                forces[i] = G*body[i].masa*body[j].masa/norm
                forcesx += forces[i] * dx / (norm ** 0.5)
                forcesy += forces[i] * dy / (norm ** 0.5)
        ax = forcesx / body[i].masa
        body[i].vx += ax * dt
        ay = forcesy / body[i].masa
        body[i].vy += ay * dt
        body[i].x += body[i].vx * dt / escala
        body[i].y += body[i].vy * dt / escala
    for i in range(len(body)):
        pygame.draw.circle(screen, body[i].color, (body[i].x, body[i].y), body[i].ratio)
    pygame.display.flip()

pygame.quit()



