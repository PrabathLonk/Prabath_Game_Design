# Prabath Girish
# 4/6/22
import mailbox
import os, time, random,math
import pygame as p
os.system('cls')
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE
#initialize pygame
p.init()
#variables, constants, and objects
WIDTH=700
HEIGHT=700
x=100
y=15
xc=random.randint(50, WIDTH-50)
yc=random.randint(50,HEIGHT-50)
hbox=20  #height if rect
wbox=20  #width of rect
rad=10    #radius of the circle
#inscribe square
ibox=rad*math.sqrt(2)
xi= xc-ibox/2
yi= yc-ibox/2
inscSq=p.Rect(xi,yi, ibox,ibox)
bg=p.image.load('FinalCircleEatSquareGame\Images\Volcano.jpg')
man=p.image.load('FinalCircleEatSquareGame\Images\Screenshot (12).png')
Glisc=p.image.load('FinalCircleEatSquareGame\Images\Screenshot (13).png')

manX=0
manY=HEIGHT-128
GliscX=WIDTH
GliscY=10
check=True
manSquare=p.Rect(manX,manY,64,64)
GliscSq=p.Rect(GliscX,GliscY,64,64)
boulder = p.Rect(230,270,180,345) 
square=p.Rect(x,y,wbox,hbox)

JUMP=False
#create screen
screen=p.display.set_mode((WIDTH,HEIGHT))

#define colors Dictionary dictio={key: values}
colors={'red':[255,0,0],'white':[255,255,255],'mag':[255,0,255],
'aqua':[51,153,255],'m':[47,192,229]}
#calling values from a dictionaty get('key')
background=colors.get('white')
cr_color=colors.get('mag')
#Create a sqaure rand color 
#sq_color=colors.get('aqua')
blColor=colors.get('aqua')
randColor=''
def changeClr():
    print(background)
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        print("rand Clr = ", randColor)
        if colors.get(randColor)  == background:
            print("backgrnd = randclr")
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
changeClr()
sq_color=colors.get(randColor)    

p.display.set_caption("Circle eats Square")
jumpCount=7
COUNT=7
impact=False
while check:
    move=10
    # crash=boulder.colliderect(manSquare)
    # if crash:
    #     impact = True
    # else:
    #     impact=False

    for case in p.event.get():
        if case.type == p.QUIT:
            check=False
    keys=p.key.get_pressed() # this is a list
    print(impact)
    if case.type==p.MOUSEBUTTONDOWN:
        mouse_pos=p.mouse.get_pos()
        print(mouse_pos)
    #Square Moves
    if keys[p.K_a] and manSquare.x>=move:
        # square.x -= move
        # if not impact:
        manX -= move
        manSquare.x -= move
    if keys[p.K_d] and manSquare.x<=WIDTH-(128+move):
        # square.x += move
        # if not impact:
        manX += move
        manSquare.x += move
    if keys[p.K_s] and manSquare.y<=HEIGHT-(128+move):
        manY += move
        manSquare.y += move
    if keys[p.K_w] and manSquare.y>=move:
        manY -= move
        manSquare.y -= move
    #JUMP CODE
    if not JUMP:
        # if keys[p.K_s]:
        #     square.y += move
        #     if not impact and manX>=HEIGHT+128 :
        #         manY += move
        #         manSquare.y += move
        # if keys[p.K_w]:
        #     square.y -= move
        #     if not impact and manX>=HEIGHT-128:
        #         manY -= move
        #         manSquare.y -= move
        if keys[p.K_SPACE]:
            JUMP=True
    else:
        if jumpCount >= -COUNT:
            square.y -= jumpCount*abs(jumpCount)/2
            manY -= jumpCount*abs(jumpCount)/2
            manSquare.y -= jumpCount*abs(jumpCount)/2
            jumpCount -=1
        else:
            jumpCount=COUNT
            JUMP=False
    
    #circle moves
    if keys[p.K_LEFT] and manSquare.x>=move:
        # square.x -= move
        # if not impact:
        GliscX -= move
        GliscSq.x -= move
    if keys[p.K_RIGHT] and manSquare.x<=WIDTH-(128+move):
        # square.x += move
        # if not impact:
        GliscX += move
        GliscSq.x += move
    if keys[p.K_DOWN] and manSquare.y<=HEIGHT-(128+move):
        GliscY += move
        GliscSq.y += move
    if keys[p.K_UP] and manSquare.y>=move:
        GliscY -= move
        GliscSq.y -= move

   # choque=square.collidepoint((xc,yc))
    choque=square.colliderect(inscSq )
    if choque:
        square.x=random.randint(50, WIDTH-50)
        square.y=random.randint(50,HEIGHT-50)
        changeClr()
        sq_color=colors.get(randColor)    

        rad +=move
        ibox=rad*math.sqrt(2)
        xi= xc-ibox/2
        yi= yc-ibox/2
        inscSq=p.Rect(xi,yi, ibox,ibox)
    #Check clide between the man and the bulder
    
    

    p.draw.rect(screen,1,manSquare)
    p.draw.rect(screen,1,GliscSq)
    p.draw.rect(screen,blColor, boulder)
    screen.blit(bg,(0,0))
    screen.blit(man,(manX,manY))
    screen.blit(Glisc,(GliscX,GliscY))
    # p.draw.rect(screen,sq_color, square)
    # p.draw.rect(screen,cr_color,inscSq)
    # p.draw.circle(screen,cr_color,(xc,yc), rad )
    p.display.update()
    p.time.delay(30)