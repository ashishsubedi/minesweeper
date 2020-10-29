import pygame,sys,random
pygame.init()

win_size = width,height = 425,439

rows,cols = 10,10
cell_w,cell_h= (width//rows),(height//cols)

screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Minesweeper")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run=False
        
        
    screen.fill(0)
    for y in range(0,height):
        for x in range(0,width):
            pygame.draw.rect(screen,(255,255,255),(x*(cell_w+1),y*(cell_h+1),cell_w,cell_h))
    pygame.display.update()

pygame.quit()