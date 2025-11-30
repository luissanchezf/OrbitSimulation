import pygame
import planetclass
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Ventana:")

p1 = planetclass.planet(200, 400,1, 1,(0,255,0), 40)

#para que no se cierre:
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    p1.x += p1.velocidadx
    p1.y += p1.velocidady
    p1.x = p1.x % 800
    p1.y = p1.y % 600
    pygame.draw.circle(screen, (0, 180, 0), (p1.x, p1.y), p1.ratio)
    pygame.display.flip()

pygame.quit()



