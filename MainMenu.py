# Prabath Girish
# 3/23/22
#Today we are going to learn how to select and use fonts
# Import pygame and os
import pygame, time, random, os
os.system('cls')
# INitialize pygame
pygame.init()
# VARIABLES
WIDTH=700
HEIGHT=700
wbox=30
hbox=30

# Menu List
menuList=['INSTRUCTIONS',"SETTINGS","PLAY GAME",'Scoreboard','Exit']
SettingList=['Screen Size', 'Font Size', 'Circle Color', 'Sound', 'Background Color']
#Define our mouse click
keys=pygame.key.get_pressed

colors={'white':[255,255,255], 'red':[255,0,0], 'orange':[255,85,0], 'purple':[48,25,52,],'aqua':[102,193,255], 'pink': [200,3,75], 'black':[0,0,0], 'navy':[5,31,64], 'white':[252,252,252], 'key lime': [198,227,171], 'seabreeze':[46,223,227]}

window=pygame.display.set_mode((WIDTH,HEIGHT))
# open a new window
window2=pygame.display.set_mode((WIDTH,HEIGHT))
#Set our caption:
pygame.display.set_caption("Circle Eat Square Menu")
# Create fonts
TITLE_FONT=pygame.font.SysFont('georgia',50) #<-- First pice of text within parenthsis is the name of the font, and the number is the height of the letters
MENU_FONT=pygame.font.SysFont('comicsans',40)
INSTRUCTION_FONT=pygame.font.SysFont('proxmanova',35)
def instructions():
    Check=True
    while Check==True:
        #Create the text we want to write
        text=TITLE_FONT.render('Circle Eat Square Instructions',1,(0,255,0)) #<-- Goes in order of actual written text, thickness, and color of the text
        instructions=INSTRUCTION_FONT.render("The goal of this game is for the player controlling the",1,(0,0,255))
        instructions2=INSTRUCTION_FONT.render("circle to catch the player controlling the square.",1,(0,0,255))
        instructions3=INSTRUCTION_FONT.render("The square controlling player uses WASD to control the",1,(0,0,255))
        instructions4=INSTRUCTION_FONT.render("square, the circle is controlled by Player 2 with the arrow",1,(0,0,255))
        instructions4=INSTRUCTION_FONT.render("keys. The square can hit space to get a vertical jump boost.",1,(0,0,255))
        instructions5=INSTRUCTION_FONT.render("Once a circle reaches a certain size, the circle player wins",1,(0,0,255))
        instructions6=INSTRUCTION_FONT.render("Try timing youself to trya get your best time as the circle",1,(0,0,255))
        BackButton=MENU_FONT.render("BACK",1,(0,0,0))
        # Put our text on screen after coloring the screen
        window.fill((255,255,255))
        #Blit is what shows and writes our text
        window2.blit(text,(20,50))
        window2.blit(instructions,(20,200))
        window2.blit(instructions2,(20,230))
        window2.blit(instructions3,(20,260))
        window2.blit(instructions4,(20,290))
        window2.blit(instructions5,(20,320))
        window2.blit(instructions6,(20,350))
        window2.blit(BackButton,(250,500))
        #Update our display 
        pygame.display.update()
        # Set a delay for us to see
        pygame.time.delay(1000)


#Creating the menu square
def MainMenu(Mlist):
    SelectX=50
    SelectY=150
    SelectSquare=pygame.Rect(SelectX,SelectY,wbox,hbox)
    SS_Color=colors.get('aqua')
    WindColor=colors.get('key lime')
    window.fill(WindColor)
    TITLE=TITLE_FONT.render("CIRCLE EAT SQUARE GAME",1,(23,123,159))
    #find the text's width to center it within the window
    xt=WIDTH/2-TITLE.get_width()/2
    window.blit(TITLE,(xt,50))
    TextY=156.5
    # Create loop to make multiple squares
    for i in range(len(Mlist)):
        message=Mlist[i]
        ClickText=INSTRUCTION_FONT.render(message,1,(0,169,184))
        window.blit(ClickText,(90,TextY))
        pygame.draw.rect(window,SS_Color,SelectSquare)
        SelectSquare.y+=75
        TextY+=75

    SelectSquare=pygame.Rect(SelectX,SelectY,wbox,hbox)
    pygame.display.update()
    pygame.time.delay(10000)

MainMenu(menuList)

def actualgame():
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

    #Getting a random color:
    RandColor=random.choice(list(colors))
    #Call colors to get colors for our screen and shapes
    background=colors.get('white')
    # s_color=colors.get('navy') <--- Previous square color
    c_color=colors.get('navy')
    Hit_color=colors.get('white')
    # Creating a color check to make sure our colors are all different:
    def ChangeColor():
        global RandColor
        ColorCheck=True
        while ColorCheck==True:
            RandColor=random.choice(list(colors)) #<--- Getting a random color for the square
            if colors.get(RandColor)==background:
                RandColor=random.choice(list(colors))
            else:
                ColorCheck=False

    ChangeColor()
    s_color=colors.get(RandColor) #<--- Getting a random color for the square


    #Define the jump function
    MAX=10
    jumpCount=MAX
    JUMP=False
    #make a function for our game
    while check:
        #Fill the screen and draw the shapes (for testing)
        screen.fill(background)
        MainMenu(menuList)
        for case in pygame.event.get():
            if case.type==pygame.QUIT:
                check=False
        #Checking for events in the pygame and allow for key inputs
        #For keys use K_(key value)
        #arrows for circle and wasd for squares
        for case in pygame.event.get():
            if case.type==pygame.QUIT:
                check=False
        keys=pygame.key.get_pressed() #<-- To check if a key gets pressed (classified as a list), the 'and move' part has to do with creating boundries
        if case.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            print(mouse_pos)
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
            RandColor=random.choice(list(colors))
            ChangeColor()
            s_color=colors.get(RandColor)

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

