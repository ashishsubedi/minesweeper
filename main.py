'''
    Author: Ashish Subedi
    File: main.py
    Description: Basic minesweeper game made using PyGame. Can be considered 2 day build. 

'''


import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


import pygame,sys,random
from pygame.locals import *
pygame.init()

# Change these for different gameplay
MINES = 30
rows,cols = 10,10

#End Change

white = (255,255,255)
gray = (150,150,150)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)


win_size = width,height = 600,600

cell_w,cell_h= (width//cols),(height//rows)

font = pygame.font.SysFont('Arial', 25)
screen = pygame.display.set_mode(win_size)

pygame.display.set_caption("Minesweeper")

run = True
firstClick = True
gameOver = False
winner = False

mines = MINES
flags = MINES

game_matrix = [[0 for i in range(cols)] for j in range(rows) ]
flagged = set()

remainingSafe = 0

def clear():
    screen.fill(black)
    for y in range(0,height,cell_h):
        for x in range(0,width,cell_w):
            
            pygame.draw.rect(screen,white,(x,y,cell_w-1,cell_h-1))
    pygame.display.update()

def reset():
    global firstClick,gameOver,mines,flags,flagged,game_matrix,remainingSafe,winner
    clear()
    firstClick = True
    gameOver= False
    flagged = set()
    game_matrix = [[0 for i in range(cols)] for j in range(rows) ]
    mines = MINES
    flags = MINES
    remainingSafe = 0
    winner = False

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
                #No of valid squares
                remainingSafe = (rows*cols)-mines
                
                #Plant mines and start calculation
                while mines > 0:
                    x_mine,y_mine = random.randint(0,cols-1),random.randint(0,rows-1)
                    
                    if(game_matrix[x_mine][y_mine] != -1 and (x_mine != x and y_mine != y) ):
                        game_matrix[x_mine][y_mine] = -1
                        mines -= 1
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

            else:
                if game_matrix[x][y] == -1:
                    #Game over Mine BOOM

                    color = red
                    gameOver = True
                    for j in range(rows):
                        for i in range(cols):
                            if game_matrix[i][j]==-1:
                                pygame.draw.rect(screen,color,(i*cell_w,j*cell_h,cell_w-1,cell_h-1))
                                #if the mine is flagged, show F
                                if((i,j) in flagged):
                                    dest_x = (i*cell_w)+(cell_w/3)
                                    dest_y = (j*cell_h)+(cell_h/3)
                                    
                                    screen.blit(font.render("F",True,black),(dest_x,dest_y))


                else:
                    if (x,y) in flagged: continue
                    # Show score on that cell
                    remainingSafe -= 1
                    score = game_matrix[x][y]
                    dest_x = (x*cell_w)+(cell_w/3)
                    dest_y = (y*cell_h)+(cell_h/3)
                    color = blue
                    
            
                    pygame.draw.rect(screen,color,(x*cell_w,y*cell_h,cell_w-1,cell_h-1))
                    screen.blit(font.render(str(score),True,black),(dest_x,dest_y))
                  

                    if( remainingSafe == 0):
                        #Winner
                        color = red
                        gameOver = True
                        winner = True

                        for j in range(rows):
                            for i in range(cols):
                                if game_matrix[i][j]==-1:
                                    pygame.draw.rect(screen,color,(i*cell_w,j*cell_h,cell_w-1,cell_h-1))
                                    #if the mine is flagged, show F
                                    if((i,j) in flagged):
                                        dest_x = (i*cell_w)+(cell_w/3)
                                        dest_y = (j*cell_h)+(cell_h/3)
                                        
                                        screen.blit(font.render("F",True,black),(dest_x,dest_y))


            #display label

        #for Flags
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not gameOver:
            #Get position
            pos = pygame.mouse.get_pos()
            #Check the cell
            x,y = pos[0]//cell_w,pos[1]//cell_h
            if firstClick: continue

            #Mine Flag it
            if(flags and (x,y) not in flagged):
                color = green
                dest_x = (x*cell_w)+(cell_w/3)
                dest_y = (y*cell_h)+(cell_h/3)

                flagged.add((x,y))

                pygame.draw.rect(screen,color,(x*cell_w,y*cell_h,cell_w-1,cell_h-1))
                screen.blit(font.render('F',True,black),(dest_x,dest_y))
                pygame.display.update()
                flags-=1
            elif((x,y) in flagged):
                color = white
                dest_x = (x*cell_w)+(cell_w/3)
                dest_y = (y*cell_h)+(cell_h/3)

                flagged.remove((x,y))

                pygame.draw.rect(screen,color,(x*cell_w,y*cell_h,cell_w-1,cell_h-1))
               
                pygame.display.update()
                flags+=1

                

    if firstClick:
        clear()        
        screen.blit(font.render(f"CLICK START GAME. {mines} Mines.{flags} Flags",True,black),(0,height/4))
    if gameOver:   
        if not winner:
            screen.blit(font.render("FOOOOSHHH!! GAME OVER. Press R",True,black),(width/10,height/4))
        else:
            screen.blit(font.render("YOOHOO! WINNER. DONE. OVER. Press R for surprise",True,black),(width/10,height/4))

    pygame.display.update()

pygame.quit()