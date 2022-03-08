# Prabath Girish
# # 3/8/22

# Learning how to draw circles and squares
# Also learning how to use keys
# Objective is for the square to rn away from the circle 
# If the circle eats the square it becomes larger and a new square will appear

import os, random, time, pygame
from turtle import circle
#Initialize pygame, you also have the option to import it as p or pg
pygame.init()

#Variables for moving
move=5 #pixels
# Declare constant variables, list, dictionaries
#Capitalize to clarify constants
#Screen size
WIDTH=700
HEIGHT=700
check=True #<-- For while loop
#Square position and size
xs=20
ys=20
wbox=30
hbox=30
# Circle radius
CRadius=15
# Circle random start point (making sure the circle doesn't appear partly offscreen)
xc=random.randint(CRadius,WIDTH-CRadius)
yc=random.randint(CRadius,HEIGHT-CRadius)
# create the objects
#Our screen:
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Circle Eats Square")
# "Rect" stands for the rectangle shape type
#The measurments go in x position, y position, width, height 
square=pygame.Rect(xs,ys,wbox,hbox)


#Create the screen
pygame.display.set_mode((WIDTH,HEIGHT))

#Define our colors in a dictionary
colors={'white':[255,255,255], 'red':[255,0,0], 'orange':[255,85,0], 'purple':[48,25,52,],'aqua':[102,193,255], 'pink': [200,3,75], 'black':[0,0,0], 'navy':[5,31,64]}

#Call colors to get colors for our screen and shapes
background=colors.get('pink')
s_color=colors.get('navy')
c_color=colors.get('white')

#Define the circle


#make a function for our game
while check:
    #Fill the screen and draw the shapes (for testing)
    screen.fill(background)
    #Checking for events in the pygame and allow for key inputs
    #For keys use K_(key value)
    #arrows for circle and wasd for squares
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() #<-- To check if a key gets pressed (classified as a list), the 'and move' part has to do with creating boundries
    if keys[pygame.K_a] and square.x>=move:
        square.x-=move #subtract
    if keys[pygame.K_d] and square.x<=WIDTH-wbox:
        square.x+=move
    if keys[pygame.K_w] and square.y>=move:
        square.y-=move
    if keys[pygame.K_s] and square.y<=HEIGHT-hbox:
        square.y+=move
    # Circle Movements
    if keys[pygame.K_LEFT] and xc>=move:
        xc-=move #subtract
    if keys[pygame.K_RIGHT] and xc<=WIDTH-CRadius:
        xc+=move
    if keys[pygame.K_UP] and yc>=move:
        yc-=move
    if keys[pygame.K_DOWN] and yc<=HEIGHT-CRadius:
        yc+=move


    pygame.draw.rect(screen,s_color,square)
    pygame.draw.circle(screen,c_color,(xc,yc),CRadius)

    #Display the screen and shapes via updating (for testing)
    pygame.display.update()
    #Add a delay so that we can see our shapes (for testing)
    pygame.time.delay(10)

