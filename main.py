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
gameOver = False

mines = 30
# flags = 20
game_matrix = [[0 for i in range(cols)] for j in range(rows) ]


def clear():
    screen.fill(black)
    for y in range(0,height,cell_h):
        for x in range(0,width,cell_w):
            
            pygame.draw.rect(screen,white,(x,y,cell_w-1,cell_h-1))
    pygame.display.update()

def reset():
    global firstClick,gameOver
    clear()
    firstClick = True
    gameOver= False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run=False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                reset()
        #Handle mouse event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not gameOver:
            #Get position
            pos = pygame.mouse.get_pos()
            #Check the cell
            x,y = pos[0]//cell_w,pos[1]//cell_h
            #Initialize game
            if firstClick:
                clear()
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
                if game_matrix[x][y] == -1:
                    #Game over Mine BOOM

                    color = red
                    pygame.draw.rect(screen,color,(x*cell_w,y*cell_h,cell_w-1,cell_h-1))
                    gameOver = True
                else:
                    # Show score on that cell
                    
                    score = game_matrix[x][y]
                    dest_x = (x*cell_w)+(cell_w/3)
                    dest_y = (y*cell_h)+(cell_h/3)
                    color = blue
                    
            
                    pygame.draw.rect(screen,color,(x*cell_w,y*cell_h,cell_w-1,cell_h-1))
                    screen.blit(font.render(str(score),True,black),(dest_x,dest_y))
                    pygame.display.update()

                    


            #display label
    if firstClick:
        clear()        
        screen.blit(font.render(f"PRESS ANY CELL TO START GAME. {mines} Mines",True,black),(width/8,height/4))
    if gameOver:   
         
        screen.blit(font.render("FOOOOSHHH!! GAME OVER. Press R",True,red),(width/8,height/4))
        
    pygame.display.update()

pygame.quit()