# Prabath Girish
# # 4/4/22
import os, random, time, pygame, math, datetime
from turtle import update
# name=input("What is your name:")
#initialize pygame
pygame.init()
WIDTH=700
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("LEVEL 2")
bg=pygame.image.load('FinalCircleEatSquareGame\Images\Volcano.jpg')
Darm=pygame.image.load('FinalCircleEatSquareGame\Images\Screenshot (12).png')
Gliscor=pygame.image.load('FinalCircleEatSquareGame\Images\Screenshot (13).png')
screen.blit(bg,(0,0))
screen.blit(Darm,(0,0))
screen.blit(Gliscor,(200,300))
pygame.display.update()
pygame.time.delay(2000)
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)
MAX=10
jumpCount=MAX
JUMP=False
HitX=xc-15
HitY=yc-15
CRadius=15
HitLenght=CRadius*2
HitWidth=CRadius*2
hitbox=pygame.Rect(HitX,HitY,HitWidth,HitLenght)
move=5
score=0
ColorCheck=False
def ActualGame():
    global move
    global check
    global screen
    global square
    global hitbox
    global c_color
    global background
    global Hit_color
    global s_color
    global jumpCount
    global JUMP
    global CRadius
    global MAX
    global HitLenght
    global HitWidth
    global changeColor
    global HitX
    global HitY
    global ColorCheck
    global score
    move=5 #pixels
    # Declare constant variables, list, dictionaries
    #Capitalize to clarify constants
    #Screen size
    ticksStart=pygame.time.get_ticks()
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

    #Getting a random color:
    RandColor=random.choice(list(colors))
    print(RandColor)
    #Call colors to get colors for our screen and shapes
    background=colors.get('aqua')
    # s_color=colors.get('navy') <--- Previous square color
    c_color=colors.get('black')
    Hit_color=colors.get('aqua')
    # Creating a color check to make sure our colors are all different:
    def changeColor():
        global randColor
        colorCheck=True
        while colorCheck:
            randColor=random.choice(list(colors))
            if colors.get(randColor)==background:
                print(randColor)
                print(background)
                randColor=random.choice(list(colors))
            else:
                colorCheck=False

    changeColor()
    s_color=colors.get('pink') #<--- Getting a random color for the square


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
        if JUMP==False:
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
            hitbox.x-=move
        if keys[pygame.K_RIGHT] and xc<=WIDTH-(CRadius+move):
            xc+=move
            hitbox.x+=move
        if keys[pygame.K_UP] and yc>=move+CRadius:
            yc-=move
            hitbox.y-=move
        if keys[pygame.K_DOWN] and yc<=HEIGHT-(CRadius+move):
            yc+=move
            hitbox.y+=move
        #Making the collision
        checkCollide= square.colliderect(hitbox)
        if checkCollide==True:
            square.x=random.randint(wbox,WIDTH-wbox)
            square.y=random.randint(hbox,HEIGHT-hbox)
            CRadius+=move
            HitWidth+=move
            HitLenght+=move
            changeColor()
            ColorCheck=True
            # RandColor=random.choice(list(colors-'aqua'))
        pygame.draw.rect(screen,s_color,square)
        pygame.draw.rect(screen,Hit_color,hitbox)
        pygame.draw.circle(screen,c_color,(xc,yc),CRadius)
        if CRadius==50:
            global ticksEnd
            print("The circle player has won the game! Congrats! Switch roles as see if you can beat that time! ")
            ticksEnd=pygame.time.get_ticks()
            score=100000-(ticksEnd-ticksStart)
            print("Your score is:",score)
        #Display the screen and shapes via updating (for testing)
        pygame.display.update()
        #Add a delay so that we can see our shapes (for testing)
        pygame.time.delay(10)
