#Prabath Girish (3/25/22)
#learning how to draw circles and rectangles
#use keys to move objects
#Using Dictionaries

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square, 
#circle will  get larger, and a new rect should appear somewhere on the screen
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               jump
#initialize pygame
import os, random, time, pygame, math
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
TITLE_FONT=pygame.font.SysFont('georgia',50) #<-- First pice of text within parenthsis is the name of the font, and the number is the height of the letters
MENU_FONT=pygame.font.SysFont('comicsans',40)
INSTRUCTION_FONT=pygame.font.SysFont('proxmanova',35)
#scree size
WIDTH=700
HEIGHT=700
xMs=50
yMs=250
wb=30
hb=30
MAIN=True
INST=False
SETT=False
GAME=False
LEV_I=False
#List f messages
MenuList=['Instructions','Settings', "Play Game","Exit",'Scoreboard']
SettingList=['Screen Size','Font Size','Circle Color','Background Color']
check=True #for the while loop
move=5 #pixels
#square variables
xs=20
ys=20
wbox=30
hbox=30
#circle variables
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)

#inscribed Square:
ibox=int(rad*math.sqrt(2))
startpoint = (int(xc-ibox/2),int(yc-ibox/2))
print(startpoint[0]-ibox,startpoint[1])
insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
#creating the rect object
square=pygame.Rect(xs,ys,wbox,hbox)

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('white')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')

#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)

#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((255,255,255))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))

#Create First button


#Create square fr menu
xSett=100
ySett=250
settW=30
SettH=30
squareM=pygame.Rect(xMs,yMs,wb,hb)
squareSet=pygame.Rect(xSett,ySett,settW,SettH)
#This is a function uses a parameter
def MainMenu(Mlist):
    global txtx
    global txty
    txty=243
    txtx=90
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(txtx,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(10)
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
def SettMenu(Mlist):
    global txtS
    global txtSS
    txtS=243
    txtSS=145
    squareSet.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(txtSS,txtS))
        pygame.draw.rect(screen,sqM_color, squareSet )
        squareSet.y +=50
        txtS+=50
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
        if CRadius==80:
            print("The circle player has won the game! Congrats! Switch roles as see if you can beat that time! ")
            check=False

        #Display the screen and shapes via updating (for testing)
        pygame.display.update()
        #Add a delay so that we can see our shapes (for testing)
        pygame.time.delay(10)
#sq_color=colors.get('navy')
#Making a rand c f the square
changeColor()
sq_color=colors.get('pink')


MAX=10
jumpCount=MAX
JUMP=False
while check:
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if SETT:
        TitleMenu("SETTINGS")
        SettMenu(SettingList)
        BackButton=MENU_FONT.render("BACK (Press ESC)",1,(0,0,0))
        screen.blit(BackButton,(200,500))
    if GAME:
        ActualGame()
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() #this returns a list
    if case.type ==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        print(mouse_pos)
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or INST :
            MAIN=False
            screen.fill(background)
            TitleMenu("INSTRUCTIONS")
            INST=True
            text=TITLE_FONT.render('Circle Eat Square Instructions',1,(0,255,0)) #<-- Goes in order of actual written text, thickness, and color of the text
            instructions=INSTRUCTION_FONT.render("The goal of this game is for the player controlling the",1,(0,0,255))
            instructions2=INSTRUCTION_FONT.render("circle to catch the player controlling the square.",1,(0,0,255))
            instructions3=INSTRUCTION_FONT.render("The square controlling player uses WASD to control the",1,(0,0,255))
            instructions4=INSTRUCTION_FONT.render("square, the circle is controlled by Player 2 with the arrow",1,(0,0,255))
            instructions4=INSTRUCTION_FONT.render("keys. The square can hit space to get a vertical jump.",1,(0,0,255))
            instructions5=INSTRUCTION_FONT.render("Once a circle reaches a certain size, the circle player wins",1,(0,0,255))
            instructions6=INSTRUCTION_FONT.render("Try timing youself to try and get your best time as the circle",1,(0,0,255))
            BackButton=MENU_FONT.render("BACK (Press ESC)",1,(0,0,0))
            screen.blit(instructions,(20,200))
            screen.blit(instructions2,(20,230))
            screen.blit(instructions3,(20,260))
            screen.blit(instructions4,(15,290))
            screen.blit(instructions5,(20,320))
            screen.blit(instructions6,(20,350))
            screen.blit(BackButton,(200,500))
            if ((mouse_pos[0] >200 and mouse_pos[0] <540) and (mouse_pos[1] >500 and mouse_pos[1] <540)):
                screen.fill(background)
                INST=False
                MAIN=True
                TitleMenu("MENU")
                MainMenu(MenuList)
        elif ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)) or SETT:
            MAIN=False
            screen.fill(background)
            SETT=True
            if ((mouse_pos[0] >200 and mouse_pos[0] <540) and (mouse_pos[1] >500 and mouse_pos[1] <540)):
                screen.fill(background)
                SETT=False
                MAIN=True
                TitleMenu("MENU")
                MainMenu(MenuList)
        elif ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)) or GAME:
            screen.fill(background)
            ActualGame()
            


#     if keys[pygame.K_a] and square.x >=move:
#         square.x -= move #substract 5 from the x value
#     if keys[pygame.K_d] and square.x <WIDTH-wbox:
#         square.x += move  
#     #Jumping part
#     if not JUMP:
#         if keys[pygame.K_w]:
#             square.y -= move
#         if keys[pygame.K_s]:
#             square.y += move   
#         if keys[pygame.K_SPACE]:
#             JUMP=True
#     else:
#         if jumpCount >=-MAX:
#             square.y -= jumpCount*abs(jumpCount)/2
#             jumpCount-=1
#         else:
#             jumpCount=MAX
#             JUMP=False

# #Finish circle
#     if keys[pygame.K_LEFT] and xc >=rad+move:
#         xc -= move #substract 5 from the x value
#         insSquare.x -= move
#     if keys[pygame.K_RIGHT] and xc <=WIDTH -(rad+move):
#         xc += move #substract 5 from the x value  
#         insSquare.x += move
#     if keys[pygame.K_DOWN] and yc <=HEIGHT-(rad+move):
#         yc += move #substract 5 from the x value
#         insSquare.y += move
#     if keys[pygame.K_UP] and yc >=rad+move:
#         yc -= move #substract 5 from the x value  
#         insSquare.y -= move
        
#     checkCollide = square.colliderect(insSquare)
#     if checkCollide:
#         square.x=random.randint(wbox, WIDTH-wbox)
#         square.y=random.randint(hbox, HEIGHT-hbox)   
#         changeColor()
#         sq_color=colors.get(randColor)
#         rad +=move
#         ibox=int(rad*math.sqrt(2))
#         startpoint = (int(xc-ibox/2),int(yc-ibox/2))
#         insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
        
    
#     pygame.draw.rect(screen, sq_color, square)
#     pygame.draw.rect(screen,cr_color, insSquare )
#     pygame.draw.circle(screen, cr_color, (xc,yc), rad)

    pygame.display.update()
    pygame.time.delay(10)