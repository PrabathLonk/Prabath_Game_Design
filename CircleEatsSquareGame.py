# Prabath Girish
# # 3/8/22

# Learning how to draw circles and squares
# Also learning how to use keys
# Objective is for the square to rn away from the circle 
# If the circle eats the square it becomes larger and a new square will appear

import os, random, time, pygame
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
#dimesions for the hitbox
HitLenght=CRadius*2
HitWidth=CRadius*2
# Circle random start point (making sure the circle doesn't appear partly offscreen)
xc=random.randint(CRadius,WIDTH-(2*CRadius))
yc=random.randint(CRadius,HEIGHT-(2*CRadius))
HitX=xc-15
HitY=yc-15
# create the objects
#Our screen:
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Circle Eats Square")
# "Rect" stands for the rectangle shape type
#The measurments go in x position, y position, width, height 
square=pygame.Rect(xs,ys,wbox,hbox)

#Dimesions of the circle hitbox
hitbox=pygame.Rect(HitX,HitY,HitWidth,HitLenght)


#Create the screen
pygame.display.set_mode((WIDTH,HEIGHT))

#Define our colors in a dictionary
colors={'white':[255,255,255], 'red':[255,0,0], 'orange':[255,85,0], 'purple':[48,25,52,],'aqua':[102,193,255], 'pink': [200,3,75], 'black':[0,0,0], 'navy':[5,31,64]}

#Call colors to get colors for our screen and shapes
background=colors.get('pink')
s_color=colors.get('navy')
c_color=colors.get('white')
Hit_color=colors.get('orange')

#Define the jump function
MAX=10
jumpCount=MAX
JUMP=False



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
    # Movements for the square
    if keys[pygame.K_a] and square.x>=move:
        square.x-=move #subtract
    if keys[pygame.K_d] and square.x<=WIDTH-(wbox+move):
        square.x+=move
    #Jumping
    if not JUMP:
        if keys[pygame.K_w] and square.y>=move:
            square.y-=move
        if keys[pygame.K_s] and square.y<=HEIGHT-(hbox+move):
            square.y+=move
        if keys[pygame.K_SPACE]:
            JUMP=True
    else:
        if jumpCount>=-MAX:
            square.y-=jumpCount*abs(jumpCount)/2
            jumpCount-=1
        else:
            jumpCount=MAX
            JUMP=False
    # Circle Movements
    if keys[pygame.K_LEFT] and xc>=move+CRadius:
        xc-=move #subtract
        HitX-=move
    if keys[pygame.K_RIGHT] and xc<=WIDTH-(CRadius+move):
        xc+=move
        HitX+=move
    if keys[pygame.K_UP] and yc>=move+CRadius:
        yc-=move
        HitY-=move
    if keys[pygame.K_DOWN] and yc<=HEIGHT-(CRadius+move):
        yc+=move
        HitY+=move
    #Making the collision
    checkCollide= square.collidepoint(xc,yc)
    if checkCollide==True:
        square.x=random.randint(wbox,WIDTH-wbox)
        square.y=random.randint(hbox,HEIGHT-hbox)
        CRadius+=move

    pygame.draw.rect(screen,s_color,square)
    pygame.draw.rect(screen,Hit_color,hitbox)
    pygame.draw.circle(screen,c_color,(xc,yc),CRadius)

    #Display the screen and shapes via updating (for testing)
    pygame.display.update()
    #Add a delay so that we can see our shapes (for testing)
    pygame.time.delay(10)

