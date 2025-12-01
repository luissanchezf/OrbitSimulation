import pygame
import planetclass
from math import cos, sin, sqrt
pygame.init()

#const:
G = 6.67430e-11
escala = 1e10  #1px = 1e10m
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Simulador de orbitas:")

sol = planetclass.planet(200, 300,(0,255,0), 10, 2e30, 0, 0)
p2 = planetclass.planet(200, 200, (255,0,0),5, 6e24,0.5 ,150*escala)
#escala
body = [sol, p2]
for i in range(1, len(body)):
    if body[i].e != 1 and body[i].a != 0:
        body[i].vy = sqrt(G * sol.masa * (1+body[i].e)/(body[i].a*(1-body[i].e)))
    body[i].vx = 0
    body[i].x = sol.x-body[i].a*(1-body[i].e)/escala
    body[i].y = sol.y
    #actualizar velocidad inicial



forces = [0, 0]
forcesx = 0
forcesy = 0
dt = 100000
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
                dx = (body[j].x-body[i].x) * escala
                dy = (body[j].y-body[i].y) * escala
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
        pygame.draw.circle(screen, body[i].color, (int(body[i].x),int(body[i].y)), body[i].ratio)
    pygame.display.flip()

pygame.quit()



