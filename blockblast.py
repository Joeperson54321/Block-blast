import pygame,sys
spaces = []
colorsr = []
colorsg = []
colorsb = []
for i in range(64):
    spaces.append(0)
    colorsr.append(10)
    colorsg.append(10)
    colorsb.append(120)
pygame.init()
pygame.display.set_caption("Block Blast")
screen = pygame.display.set_mode((800,500))
def drawSquare(x,y,r,g,b,len):
    pygame.draw.rect(screen,(r,g,b),pygame.Rect(x,y,len,len))
def drawGridSquares():
    for i in range(8):
        for j in range(8):
            index =i*8+j
            drawSquare(50+j*25,50+i*25,colorsr[index],colorsg[index],colorsb[index],20)
def drawGridLines():
    print("left")
drawSquare(100,100,255,0,0,50)
#pygame.draw.rect(screen,(100,100,50),pygame.Rect(50,50,50,50)) 
while True:
    #pygame.quit()
    screen.fill((0,0,0))
    drawGridSquares()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
