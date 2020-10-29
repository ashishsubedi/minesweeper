import pygame,sys,random
from pygame.locals import *
pygame.init()

white = (255,255,255)
gray = (150,150,150)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)


win_size = width,height = 600,600

rows,cols = 10,10
cell_w,cell_h= (width//cols),(height//rows)

font = pygame.font.SysFont('Arial', 25)
screen = pygame.display.set_mode(win_size)

pygame.display.set_caption("Minesweeper")

run = True
firstClick = True

mines = 20
flags = 20

game_matrix = [[0 for i in range(cols)] for j in range(rows) ]
print(game_matrix)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run=False
        #Handle mouse event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #Get position
            pos = pygame.mouse.get_pos()
            #Check the cell
            x,y = pos[0]//cell_w,pos[1]//cell_h
            #Initialize game
            if firstClick:
                firstClick = False
                
                #Plant mines and start calculation
                while mines > 0:
                    x_mine,y_mine = random.randint(0,cols-1),random.randint(0,rows-1)
                    
                    if(game_matrix[x_mine][y_mine] != -1 and (x_mine != x and y_mine != y) ):
                        game_matrix[x_mine][y_mine] = -1
                        mines -= 1
                print("MINES:",game_matrix)
                for j in range(rows):
                    for i in range(cols):
                        if(game_matrix[i][j] == -1): continue
                        mine_count = 0
                        for a in [-1,0,1]:
                            for b in [-1,0,1]:
                                if(i+a>=0 and i+a < cols and j+b>=0 and j+b<rows): 
                                    if(game_matrix[i+a][j+b] == -1):
                                        mine_count+=1
                        
                        game_matrix[i][j] = mine_count
                print("FINAL: ",game_matrix)           

            else:
                if(game_matrix[x][y]>0): continue
                elif game_matrix[x][y] == -1:
                    #Game over Mine BOOM
                    pass 
                else:
                    # game_matrix
                    pass


            #display label
    screen.fill(black)
    # if firstClick:
    for y in range(0,height,cell_h):
        for x in range(0,width,cell_w):
            i,j = x//cell_w,y//cell_h
    
            color = blue
            if(game_matrix[i][j] == 0): color = white
            elif(game_matrix[i][j] == -1): color = red
        
            pygame.draw.rect(screen,color,(x,y,cell_w-1,cell_h-1))
            
    pygame.display.update()

pygame.quit()