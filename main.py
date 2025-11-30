import pygame
import planetclass
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Ventana:")

p1 = planetclass.planet(200, 400,(0,255,0), 40)

#para que no se cierre:
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0, 255, 0), (p1.x, p1.y), p1.ratio)
    pygame.display.flip()

pygame.quit()



