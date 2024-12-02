import pygame,sys
spaces = []
colorsr = []
colorsg = []
colorsb = []
colorsr_2 = []
colorsg_2 = []
colorsb_2 = []

for i in range(64):
    spaces.append(0)
    colorsr.append(10)
    colorsg.append(10)
    colorsb.append(120)
    colorsr_2.append(0)
    colorsg_2.append(0)
    colorsb_2.append(0)
pygame.init()
pygame.display.set_caption("Block Blast")
screen = pygame.display.set_mode((580,750))
def drawSquare(x,y,r,g,b,len):
    pygame.draw.rect(screen,(r,g,b),pygame.Rect(x,y,len,len))
def background_square(x,y,r,g,b,len):
    pygame.draw.rect(screen,(r,g,b),pygame.Rect(x,y,len,len))
def drawGridSquares():
    for i in range(8):
        for j in range(8):
            index =i*8+j
            drawSquare(130+j*45,115+i*45,colorsr[index],colorsg[index], colorsb[index],45)
            background_square(140+j*42,125+i*42,colorsr_2[index],colorsg_2[index],colorsb_2[index],40)
def drawGridLines():
    print("left")
drawSquare(100,100,0,0,0,50)
background_square(100,100,0,0,0,50)
#pygame.draw.rect(screen,(100,100,50),pygame.Rect(50,50,50,50))
while True:
    #pygame.quit()
    screen.fill((0,64,255))
    drawGridSquares()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
