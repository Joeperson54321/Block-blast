import pygame
pygame.init()
pygame.display.set_caption("Block Blast")
screen = pygame.display.set_mode((400,300))
def drawSquare(x,y,r,g,b,len):
    pygame.draw.rect(screen,(r,g,b),pygame.Rect(x,y,len,len))
drawSquare(100,100,200,100,100,50)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
pygame.quit()
