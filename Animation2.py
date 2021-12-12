#Loops Assignment
##Application - Level 4+
import os
import pygame
import random

# the following code will always put the screen in the top corner
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)

import pygame   
pygame.init()
SIZE = (700, 700)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode(SIZE)

# Draws a black square gradually getting smaller
for xy in range(700, 0, -1): ##to get smaller, xy must decrease, starting from 700
    if xy > 0:
        pygame.draw.rect(screen, (random.randint (0 , 255), random.randint (0 , 255), random.randint (0 , 255)), (0, 0, xy+1, xy+1)) ##the coloured square it leaves behind 
        pygame.draw.rect(screen, BLACK, (0, 0, xy, xy)) ##the square itself
        pygame.event.get()     
        pygame.display.flip()
    
# Draws a black square gradually getting bigger
for xy in range(0, 700): ##to get bigger, xy must increase, starting from 0
    pygame.draw.rect(screen, (random.randint (0 , 255), random.randint (0 , 255), random.randint (0 , 255)), (0, 0, xy+1, xy+1))  ##the coloured square the black square engulfs   
    pygame.draw.rect(screen, BLACK, (0, 0, xy, xy)) ##the square itself
    pygame.event.get()
    pygame.display.flip() 

# Draws a two coloured squares gradually getting bigger     
for xy in range(0, 350): 
    if xy > 0:
        random_colour = (random.randint (0 , 255), random.randint (0 , 255), random.randint (0 , 255)) ##Makes sure that that the random colours of the top square and bottom square are the same
        ##The borders ensure that the smaller squares can be seen overtop of the bigger squares
        pygame.draw.rect(screen, random_colour, (0, 350, xy, xy), 1) ##bottom square
        pygame.draw.rect(screen, random_colour, (350, 0, xy, xy), 1) ##top square
        pygame.event.get()
        pygame.display.flip()
        pygame.time.wait(10)
    
pygame.time.wait(2)
pygame.quit()
