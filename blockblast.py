import pygame,sys
spaces = []
colorsr = []
colorsg = []
colorsb = []
rows = []
columns = []
moveindex=-1


for i in range(64):
   spaces.append(0)
   colorsr.append(10)
   colorsg.append(10)
   colorsb.append(120)
pygame.init()
pygame.display.set_caption("Block Blast")
screen = pygame.display.set_mode((580,500))
def drawSquare(x,y,r,g,b,len):
   pygame.draw.rect(screen,(r,g,b),pygame.Rect(x,y,len,len))
def background_square(x,y,r,g,b,len):
   pygame.draw.rect(screen,(r,g,b),pygame.Rect(x,y,len,len))
def drawGridSquares():
   for i in range(8):
       for j in range(8):
           index =i*8+j
           drawSquare(50+j*35,115+i*35,colorsr[index],colorsg[index], colorsb[index],32)
def generateBlocks():
    for z in range(1):
       if(z==moveindex):
           drawSquare(mousex-offsetx-3,mousey-offsety-3,0,0,0,73)
       else:
           drawSquare(367,132,0,0,0,73)
       for i in range(2):
           for j in range(2):
               if(z==moveindex):
                   drawSquare(mousex-offsetx+j*35,mousey-offsety+i*35,255,0,0,32)
               else:
                   drawSquare(370+j*35,135+i*35,255,0,0,32)
def checkCollisions():
   global offsetx
   global offsety
   if(not mousedown):
       if (moveindex !=-1):
           tempx = mousex-offsetx-50
           tempy = mousey-offsety-115
           index_x = round(tempx/35)
           index_y = round(tempy/35)
           #print(index_x)
           #print(index_y)
           if(index_x<=6 and index_x>=0 and index_y<=7 and index_y>=0):


               #makes sure that the space dosent already have something in it
               if(
               spaces[index_y*8+index_x] == 0 and
               spaces[index_y*8+(index_x+1)] == 0 and
               spaces[(index_y+1)*8+(index_x+1)] == 0 and
               spaces[(index_y+1)*8+(index_x)] == 0):
                   #puts block in the open space and gives it the value of 1
                   spaces[index_y*8+index_x]=1
                   spaces[index_y*8+(index_x+1)]=1
                   spaces[(index_y+1)*8+(index_x+1)]=1
                   spaces[(index_y+1)*8+(index_x)]=1


                   #the colors and shit
                   colorsr[index_y*8+index_x]=255
                   colorsr[index_y*8+(index_x+1)]=255
                   colorsr[(index_y+1)*8+(index_x+1)]=255
                   colorsr[(index_y+1)*8+(index_x)]=255
                   colorsg[index_y*8+index_x]=1
                   colorsg[index_y*8+(index_x+1)]=1
                   colorsg[(index_y+1)*8+(index_x+1)]=1
                   colorsg[(index_y+1)*8+(index_x)]=1
                   colorsb[index_y*8+index_x]=1
                   colorsb[index_y*8+(index_x+1)]=1
                   colorsb[(index_y+1)*8+(index_x+1)]=1
                   colorsb[(index_y+1)*8+(index_x)]=1
       return -1
   elif(moveindex==-1):
       if(mousedown and mousex<450 and mousex>370 and mousey>135 and mousey<205):
           offsetx = mousex-370
           offsety = mousey-135
           return 0
   else:
       return moveindex

def check_for_completed_lines():
    # Check for completed rows
    for row in range(8):
        if all(spaces[row * 8 + col] == 1 for col in range(8)):  # If all values in the row are 1
            clear_row(row)

    # Check for completed columns
    for col in range(8):
        if all(spaces[row * 8 + col] == 1 for row in range(8)):  # If all values in the column are 1
            clear_column(col)

def clear_row(row):
    # Set the entire row to 0 (clear the row)
    for col in range(8):
        spaces[row * 8 + col] = 0
        colorsr[row * 8 + col] = 10
        colorsg[row * 8 + col] = 10
        colorsb[row * 8 + col] = 120

def clear_column(col):
    # Set the entire column to 0 (clear the column)
    for row in range(8):
        spaces[row * 8 + col] = 0
        colorsr[row * 8 + col] = 10
        colorsg[row * 8 + col] = 10
        colorsb[row * 8 + col] = 120





offsetx = 0
offsety = 0
while True:
   mousex = pygame.mouse.get_pos()[0]
   mousey = pygame.mouse.get_pos()[1]
   mousedown = pygame.mouse.get_pressed()[0]
   screen.fill((0,64,255))
   drawSquare(47,112,0,0,0,283)
   drawGridSquares()
   check_for_completed_lines()
   moveindex = checkCollisions()
   generateBlocks()
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()


