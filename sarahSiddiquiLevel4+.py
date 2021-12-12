#Loops Assignment
##Thinking - Level 4+
import os
import random
from pygame import * 
init()

# the following code will always put the screen in the top corner
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 0)

size = width, height = 700, 700
screen = display.set_mode(size)
button = 0
numLines = 0 ##counts the number of times a line has been drawn
tick1 = 0 ##This is the tick before the while line is drawn
timerOn = 0 ##This shows that the timer is not on yet
##ensures that the line for the first point always starts at the origin
ax = 0
ay = 0
bx = 0
by = 0 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MOON_WHITE = (232, 229, 213)
RED = (252, 71, 71)
ORANGE = (224, 93, 0)
YELLOW = (255, 220, 117)
GREEN = (8, 102, 8)
BLUE = (0, 47, 166)
SEA_COLOUR = (7, 28, 82)
LIGHT_BLUE = (148, 192, 255)
MOON_SHADOW_BLUE = (91, 116, 181)
PURPLE = (217, 176, 255)
DARK_PURPLE = (119, 51, 255)
PINK = (255, 148, 239)
choices = (YELLOW, WHITE, BLUE) ##used if the user right clicks
starChoices = (PINK, PURPLE, ORANGE, RED, BLUE, LIGHT_BLUE, BLUE, WHITE, YELLOW)
colour = WHITE

def drawStar (x, y):
    draw.polygon (screen, colour, ((x+4, y), (x, y+8), (x-4, y), (x, y-8))) ###draws a diamond-shaped star
    
def drawTwinkleStar (x, y):
    draw.polygon (screen, DARK_PURPLE, ((x, y-15), (x-3, y-3), (x-13, y), (x-3, y+3), (x, y+30), (x+3, y+3), (x+13, y), (x+3, y-3))) ###draws another type of star

def drawBackground ():
    #Sky
    screen.fill (BLACK)
    for x in range (200): ###draws the background stars 
        draw.circle (screen, WHITE, ((random.randint(0, 700)), (random.randint(0, 300))), random.randint(2, 6)) ###ensures that the background is different everytime (to portray different stars twinkling)
    #Moon
    draw.circle(screen, MOON_WHITE, (350, 240), 50) ###draws moon  
    #Sea
    draw.rect (screen, SEA_COLOUR, (0, 300, 700, 400)) ###draws the sea   
    #Moon Shadow
    for xy in range (0, 400, 20):       
        draw.rect (screen, MOON_SHADOW_BLUE, (300-xy, 300+xy, 100+(xy*2), 4)) 
        draw.rect (screen, WHITE, ((300-(xy+10)), (300+(xy+10)), (100+((xy+10)*2)),1)) 

def drawScene(screen, button, numLines, colour, ax, ay, bx, by, mousePosition): 
    #Creates the guildline that the left mouse button must be down
    if button == 1:
        ##Creates the guildline that no lines have been drawn
        if numLines == 0:
            bx, by = ax, ay ###the previous point become the present point
            ax, ay = mousePosition ###the present point becomes where the mouse's position is     
            draw.line (screen, colour, (ax, ay), (bx, by)) ###draws line from the present point to where the mouse's position is
            drawStar (ax, ay) ##draws a star the end of the line
            drawStar (bx, by) ##draws a star at the beginning of the line
            numLines += 1 ###adds one to numLines so that it knows that a line has already been drawn
        ##Creates the guildline that only one line has been drawn
        elif numLines == 1:
            cx, cy = bx, by ###makes the latest point the previous point
            bx, by = ax, ay ###the present point becomes where the mouse's position is  
            ax, ay = mousePosition ###draws line from the present point to where the mouse's position is
            draw.line (screen, colour, (ax, ay), (bx, by)) ###draws line from the present point to where the mouse's position is
            drawStar (ax, ay) ##draws a star the end of the line
            numLines += 1 ###adds one to numLines so that it knows that two lines have already been draw
        ##Creates the guildline that the second line is still present
        else:
            dx, dy = e.pos ###defines "d" any point that is clicked within the two second period 
            drawTwinkleStar (dx, dy) ###draws a twinkly star at "d"
    #Creates the guildline that the right mouse button must be down
    if button == 3: 
        colour = random.choice(choices) ##renames colour to be one of the choices everytime the user right clicks
    event.get  
    display.flip() 
    return numLines, colour, ax, ay, bx, by #updates the variables
running = True
myClock = time.Clock()


drawBackground ()
# Game Loop
while running:                              
    for e in event.get():  # checks all events that happen              
        if e.type == QUIT:        
            running = False
        if e.type == MOUSEBUTTONDOWN:
            button = e.button  
            numLines, colour, ax, ay, bx, by = drawScene(screen, button, numLines, colour, ax, ay, bx, by, e.pos) ##draws the screen and returns the varaible pretaining to the function
            #Creates the guidline that there must be two lines drawn and the timer must not begin yet
            if (numLines == 2) and (timerOn == 0): 
                tick1 = time.get_ticks() ##returns the number of ticks which is then saved into tick1
                timerOn = 1 ##turns timer on
    if numLines == 2:
        tick2 = time.get_ticks() ####returns the number of ticks which is then saved into tick2
         #Creates the guidline that the two seconds must pass
        if tick2 > (tick1 + 2000): 
            drawBackground () ##resets the screen
            draw.line (screen, colour, (ax, ay), (bx, by)) ##redraws the more recent line
            drawStar (ax, ay) ##draws a star the end of the line
            drawStar (bx, by) ##draws a star at the beginning of the line            
            event.get
            display.flip()
            numLines = 1 ## shows that only one line has been displayed
            timerOn = 0 ##turns the timer off
    myClock.tick(60)             # waits long enough to have 60 fps

quit()