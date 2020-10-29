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
            print("pressed x,y" ,x,y)
            game_matrix[x][y] = 1

            #Initialize game
            #Plant mines and start calculation
            #display label
    screen.fill(black)
    for y in range(0,height,cell_h):
        for x in range(0,width,cell_w):
            i,j = x//cell_w,y//cell_h
    
            color = blue
            if(game_matrix[i][j] == 0): color = white
            elif(game_matrix[i][j] == -1): color = red
           
            pygame.draw.rect(screen,color,(x,y,cell_w-1,cell_h-1))
            
    pygame.display.update()

pygame.quit()