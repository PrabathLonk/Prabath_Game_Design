# Prabath Girish
# 3/23/22
#Today we are going to learn how to select and use fonts
# Import pygame and os
import pygame, time, random
# INitialize pygame
pygame.init()
# VARIABLES
WIDTH=700
HEIGHT=700
wbox=30
hbox=30

# Menu List
menuList=['INSTRUCTIONS (Press 1)',"SETTINGS (Press 2)","LEVEL 1 (Press 3)","LEVEL 2 (Press 4)", "LEVEL 3 (Press 5)",'Scoreboard (Press 6)','Exit (Press 7)']

#Define our mouse click
keys=pygame.key.get_pressed

colors={'white':[255,255,255], 'red':[255,0,0], 'orange':[255,85,0], 'purple':[48,25,52,],'aqua':[102,193,255], 'pink': [200,3,75], 'black':[0,0,0], 'navy':[5,31,64], 'white':[252,252,252], 'key lime': [198,227,171], 'seabreeze':[46,223,227]}
#Getting a random color:
RandColor=random.choice(list(colors))
#Call colors to get colors for our screen and shapes
background=colors.get('white')
# s_color=colors.get('navy') <--- Previous square color
c_color=colors.get('navy')
Hit_color=colors.get('white')
# SCREEN/Set our window size
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
        for case in pygame.event.get():
            if case.type==pygame.QUIT:
                Check=False

#Creating the menu square
xs=50
ys=150
SelectSquare=pygame.Rect(xs,ys,wbox,hbox)
SelectSquare=pygame.Rect(xs,ys,wbox,hbox)
SS_Color=colors.get('aqua')
WindColor=colors.get('key lime')
window.fill(WindColor)
TITLE=TITLE_FONT.render("CIRCLE EAT SQUARE GAME",1,(23,123,159))
#find the text's width to center it within the window
xt=WIDTH/2-TITLE.get_width()/2
window.blit(TITLE,(xt,50))
TextY=156.5
# Create loop to make multiple squares
for i in range(7):
    message=menuList[i]
    ClickText=INSTRUCTION_FONT.render(message,1,(0,169,184))
    window.blit(ClickText,(90,TextY))
    pygame.draw.rect(window,SS_Color,SelectSquare)
    SelectSquare.y+=75
    TextY+=75

SelectSquare=pygame.Rect(xs,ys,wbox,hbox)
pygame.display.update()
pygame.time.delay(10000)

def clickBox():
    if keys[pygame.K_1]:
        instructions()
