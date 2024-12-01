import pygame
pygame.init()
pygame.display.set_caption("Block Blast")
screen = pygame.display.set_mode((400,300))
pygame.draw.rect(screen,(25,50,50),pygame.Rect(100,100,50,50))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
pygame.quit()
